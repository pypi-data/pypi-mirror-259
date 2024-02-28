import json
import logging
from pathlib import Path
from typing import Any, Self
from ipywidgets import jsdlink

import dema
import ipyvuetify as v
import traitlets as t
from dema.engine import DataEngine
from dema.front.logger import Logger, OutputWidgetHandler
from dema.utils.utils_misc import import_class


class App(v.App, Logger):
    def __init__(self, *, engine: DataEngine, app: bool | None = True):
        self.app = app
        self.engine = engine
        self.app_bar = AppBar(engine=engine, app=app)
        self.tree_view = TreeView(engine.front_structure_path)
        self.navigation_drawer = v.NavigationDrawer(
            app=app, v_model=True, clipped=True, children=[self.tree_view]
        )
        self.content = v.Content()  # class_="px-1 py-0"

        handler = OutputWidgetHandler(self.app_bar.logger_badge)
        handler.setFormatter(
            logging.Formatter("%(asctime)s - [%(levelname)s] %(message)s", "%H:%M:%S")
        )
        dema.logger.addHandler(handler)

        self.logger_w = handler.text_area
        self.linear_progess = v.ProgressLinear(
            color="primary", indeterminate=True, class_="d-none"
        )
        self.logger_bottom_sheet = v.BottomSheet(
            v_model=False, children=[self.linear_progess, self.logger_w]
        )

        super().__init__(
            children=[
                self.app_bar,
                self.navigation_drawer,
                self.content,
                self.logger_bottom_sheet,
            ]
        )

        self.logger_w.observe(self.on_change_text_area, names="v_model")
        self.app_bar.logger_icon.on_event("click", self.toggle_logger)
        self.app_bar.nav_icon.on_event("click", self.toggle_navigation_drawer)
        self.tree_view.observe(self.on_click_treeview, names="activated")
        self.logger_w.on_event("click:clear", self._on_click_clear_text_area)

    def _on_click_clear_text_area(self, *args) -> None:
        self.logger_bottom_sheet.v_model = False

    def toggle_logger(self, *args) -> None:
        # self.logger_bottom_sheet.class_list.toggle('d-none')
        self.logger_bottom_sheet.v_model = not self.logger_bottom_sheet.v_model

        # reset log counter
        self.app_bar.logger_badge.v_model = False

    def toggle_navigation_drawer(self, *args) -> None:
        self.navigation_drawer.v_model = not self.navigation_drawer.v_model

        # usefull only in app=False aka debug
        if not self.app:
            if self.navigation_drawer.v_model:
                self.navigation_drawer.show()
            else:
                self.navigation_drawer.hide()

    def on_click_treeview(self, change: dict) -> None:
        new = change["new"]
        if new:
            if new[0] is not None:
                class_path = new[0]["class"]
                args = new[0].get("args", [])
                kwargs = new[0].get("kwargs", {})
                class_instance = import_class(class_path)(self.engine, *args, **kwargs)
                self.content.children = [
                    class_instance.ui if hasattr(class_instance, "ui") else class_instance
                ]
        else:
            self.content.children = []

    def on_change_text_area(self, change: dict) -> None:
        self.app_bar.logger_icon.disabled = not bool(change.get("new"))

    def display_in_dialog(self, *, v_model: bool = True):
        # wrap the App instance inside a Dialog in fullscreen to be used inside jupyter
        dialog = v.Dialog(
            v_model=v_model,
            fullscreen=True,
            persistent=True,
            no_click_animation=True,
            retain_focus=False,
            v_slots=[
                {
                    "name": "activator",
                    "variable": "x",
                    "children": v.Btn(v_on="x.on", children=["Open App"]),
                }
            ],
            children=[v.Card(children=[self])],
        )

        def toggleLoading(*args) -> None:
            dialog.v_model = not dialog.v_model

        dialog.on_event("keydown.esc", toggleLoading)

        return dialog


class AppBar(v.AppBar, Logger):
    def __init__(self, *, engine: DataEngine, app: bool | None = False):
        self.engine = engine
        self.nav_icon = v.AppBarNavIcon()
        self.logger_icon = v.Icon(children=["mdi-book-open-outline"])
        self.logger_badge = v.Badge(
            bottom=True,
            v_model=False,
            color="red",
            v_slots=[
                {
                    "name": "badge",
                    "children": ["!"],
                }
            ],
            children=[self.logger_icon],
            class_="mx-5",
        )
        self.search = v.Combobox(
            v_model=None,
            item_value="class",
            label=f"Explore {engine.name} ...",
            rounded=True,
            clearable=True,
            single_line=True,
            light=True,
            background_color="white",
            class_="mt-5",
        )

        self.left_btn = v.Icon(
            children=["mdi-arrow-left"], icon=True, disabled=True, class_="pl-2"
        )
        self.right_btn = v.Icon(
            children=["mdi-arrow-right"], icon=True, disabled=True, class_="pl-2"
        )
        self.reload_btn = v.Icon(
            children=["mdi-reload"], icon=True, disabled=True, class_="pl-2"
        )

        version_chip = v.Chip(
            children=[f"v.{dema.__version__}"], outlined=True, class_="ml-2"
        )
        env_chip = v.Chip(children=[self.engine.env], outlined=True, class_="ml-2")

        super().__init__(
            app=app,
            dark=True,
            clipped_left=True,
            clipped_right=True,
            color="primary",
            children=[
                self.nav_icon,
                v.ToolbarTitle(children=[engine.name]),
                v.Spacer(),
                self.search,
                v.Col(
                    children=[
                        v.Row(
                            style_="flex-wrap:nowrap",
                            children=[self.left_btn, self.right_btn, self.reload_btn],
                        )
                    ]
                ),
                self.logger_badge,
                version_chip,
                env_chip,
            ],
        )


class TreeView(v.Treeview, Logger):
    # active is a trait from v.Treeview, event from the front are handled with `update:active`
    # but self.active is not sync on the back (BUG ??)
    # The workaound is to create another trait: `activated` that is jsdlink with `active`
    activated = t.List(t.Any(), default_value=None, allow_none=True).tag(sync=True)
    
    def __init__(self, treeview_path: Path | None):
        if treeview_path and treeview_path.exists():
            items = json.loads(treeview_path.read_text())
        else:
            items = []

        # this is used to need which node get opened
        self.previous_open_ids: list[str] = []
        super().__init__(
            items=items,
            dense=True,
            open_on_click=True,
            activatable=True,
            transition=True,
            return_object=True,
        )

        def _on_update_active(
            widget: Self, event: str, data: list[Any | None]
        ) -> None:
            # there is a bug `active is not properly sync`
            widget.__dict__["_trait_values"]["active"] = data
            widget.activated = data if data else []

        jsdlink((self, "active"), (self, "activated"))
        self.on_event("update:active", _on_update_active)
