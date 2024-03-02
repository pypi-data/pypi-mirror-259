#!/usr/bin/env python3
"""Wirebonding GUI for PSB."""

import sys
import json
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, GLib

try:
    import itkdb_gtk
    
except ImportError:
    from pathlib import Path
    cwd = Path(sys.argv[0]).parent.parent
    sys.path.append(cwd.as_posix())

from itkdb_gtk import dbGtkUtils
from itkdb_gtk import ITkDBlogin, ITkDButils, UploadTest

test_parameters = {
        "Repaired Row 1": "REPAIRED_FRONTEND_ROW1",
        "Failed Row 1": "FAILED_FRONTEND_ROW1",
        "Repaired Row 2": "REPAIRED_FRONTEND_ROW2",
        "Failed Row 2": "FAILED_FRONTEND_ROW2",
        "Repaired Row 3": "REPAIRED_FRONTEND_ROW3",
        "Failed Row 3": "FAILED_FRONTEND_ROW3",
        "Repaired Row 4": "REPAIRED_FRONTEND_ROW4",
        "Failed Row 4": "FAILED_FRONTEND_ROW4",
        "Repaired Hyb->PB": "REPAIRED_HYBRID_TO_PB",
        "Failed HyB->PB": "FAILED_HYBRID_TO_PB",
        "Repaired Module->Frame": "REPAIRED_MODULE_TO_FRAME",
        "Failed Module->Frame": "FAILED_MODULE_TO_FRAME"
}


class WireBond(Gtk.Window):
    """Main window."""

    def __init__(self, session=None, title=""):
        """Initialization."""
        super().__init__(title=title)
        self.pdb = None
        self.session = session
        self.models = {}
        self.prepare_window()

    def prepare_window(self):
        """Creates the GUI."""
        self.hb = Gtk.HeaderBar()
        self.hb.set_show_close_button(True)
        self.hb.props.title = "Wire Bond"
        self.set_titlebar(self.hb)

        # Button to upload
        button = Gtk.Button()
        icon = Gio.ThemedIcon(name="document-send-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button.add(image)
        button.set_tooltip_text("Click to upload test")
        button.connect("clicked", self.upload_test)
        self.hb.pack_end(button)

        button = Gtk.Button()
        icon = Gio.ThemedIcon(name="document-save-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button.add(image)
        button.set_tooltip_text("Click to save test file")
        button.connect("clicked", self.save_test)
        self.hb.pack_end(button)

        # Create the main box and add it to the window
        self.mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.mainBox.set_property("margin-left", 6)
        self.mainBox.set_property("margin-right", 6)
        self.add(self.mainBox)

        # Data panel
        grid = Gtk.Grid(column_spacing=5, row_spacing=1)
        for i, tit in enumerate(["Operator", "Bond Machine", "Wire Batch", "SN"]):
            lbl = Gtk.Label(label=tit)
            lbl.set_xalign(0)
            grid.attach(lbl, 0, i, 1, 1)

        self.operator = dbGtkUtils.new_small_text_entry()
        self.machine = dbGtkUtils.new_small_text_entry()
        self.batch = dbGtkUtils.new_small_text_entry()
        self.SN = dbGtkUtils.new_small_text_entry()

        grid.attach(self.operator,  1, 0, 1, 1)
        grid.attach(self.machine,   1, 1, 1, 1)
        grid.attach(self.batch,     1, 2, 1, 1)
        grid.attach(self.SN,        1, 3, 1, 1)

        self.mainBox.pack_start(grid, True, True, 0)

        # Prepare combo and all the models
        lbl = Gtk.Label(label="Choose section.")
        lbl.set_xalign(0)
        self.mainBox.pack_start(lbl, True, True, 0)

        combo = self.create_combo()
        self.mainBox.pack_start(combo, True, True, 0)

        # The tree view
        scrolled = self.create_tree_view()
        self.mainBox.pack_start(scrolled, True, True, 5)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.mainBox.pack_start(box, False, False, 0)
        dbGtkUtils.add_button_to_container(box, "Add Item",
                                           "Click to add a new item.",
                                           self.add_item)

        #
        # The text view and buffer
        #
        self.message_panel = dbGtkUtils.MessagePanel(size=100)
        self.mainBox.pack_start(self.message_panel.frame, True, True, 0)
        self.write_message("wirebond GUI")

        # The button box
        btnBox = Gtk.ButtonBox(orientation=Gtk.Orientation.HORIZONTAL)

        btn = Gtk.Button(label="Quit")
        btn.connect("clicked", self.quit)
        btnBox.add(btn)

        self.mainBox.pack_end(btnBox, False, True, 0)
        self.show_all()

    def on_name_combo_changed(self, combo):
        """Change model in TreeView."""
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            param = model[tree_iter][1]
            view_model = self.models[param]
            self.tree.set_model(view_model)
        else:
            self.write_message("Cannot find model for {}".format(param))

    def create_combo(self):
        """Create the combo."""
        model = Gtk.ListStore(str, str)
        for txt, param in test_parameters.items():
            model.append([txt, param])

            M = Gtk.ListStore(str, str)
            M.append(["", ""])
            self.models[param] = M

        self.combo = Gtk.ComboBox.new_with_model_and_entry(model)
        self.combo.set_entry_text_column(0)
        self.combo.set_active(0)
        self.combo.connect("changed", self.on_name_combo_changed)
        return self.combo

    def create_tree_view(self, size=150):
        """Creates the tree vew with the attachmens."""
        tree_iter = self.combo.get_active_iter()
        combo_model = self.combo.get_model()
        param = combo_model[tree_iter][1]
        model = self.models[param]

        self.tree = Gtk.TreeView(model=model)
        self.tree.connect("button-press-event", self.button_pressed)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.tree)
        scrolled.set_size_request(-1, size)

        renderer = Gtk.CellRendererText()
        renderer.set_property("editable", True)
        renderer.connect("edited", self.channel_edited)
        column = Gtk.TreeViewColumn("Channel", renderer, text=0)
        self.tree.append_column(column)

        renderer = Gtk.CellRendererText()
        renderer.set_property("editable", True)
        renderer.connect("edited", self.failure_edited)
        column = Gtk.TreeViewColumn("Failure", renderer, text=1)
        self.tree.append_column(column)

        return scrolled

    def text_edited(self, icol, path, text):
        """Text has been edited in the TreeView"""
        if len(text) == 0:
            return

        model = self.tree.get_model()

        n_child = model.iter_n_children()
        current_child = int(path)
        if n_child-current_child == 1:
            model.append(["", ""])

        model[path][icol] = text

    def channel_edited(self, widget, path, text):
        """Handles edition in channel number cell."""
        if not text.isnumeric():
            dbGtkUtils.complain("Wrong channel number", "Invalid channel number: {}".format(text))
            return

        self.text_edited(0, path, text)

    def failure_edited(self, widget, path, text):
        """Handles edition in comment."""
        self.text_edited(1, path, text)

    def button_pressed(self, *args):
        pass

    def add_item(self, *args):
        """Adds a new item in the current model."""
        out = dbGtkUtils.get_a_list_of_values("Add Item", ["Channel", "Comment"])
        model = self.tree.get_model()
        n_child = model.iter_n_children()
        model[-1] = out
        model.append(["", ""])

    def quit(self, *args):
        """Quits the application."""
        if self.pdb:
            self.pdb.die()
            
        self.hide()
        self.destroy()

    def write_message(self, text):
        """Writes text to Text Viewer."""
        self.message_panel.write_message(text)

    def get_list_of_channels(self, data):
        """Creates the lists of channels."""
        for key, model in self.models.items():
            iter = model.get_iter_first()
            out = {}
            while iter:
                chan, comm = model[iter]
                if len(chan) > 0:
                    out[chan] = comm
                    
                iter = model.iter_next(iter)

            data["results"][key] = out
            
    def save_test(self, *args):
        """Save Test file."""
        dialog = Gtk.FileChooserDialog(
            title="Please choose a file", parent=self, action=Gtk.FileChooserAction.SAVE
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )
        filter_text = Gtk.FileFilter()
        filter_text.set_name("JSON files")
        filter_text.add_mime_type("application/json")
        dialog.add_filter(filter_text)
        
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            ofile = dialog.get_filename()
            data = self.get_test_data()
            with open(ofile, 'w') as of:
                json.dump(data, of, indent=3)
                
        dialog.hide()
        dialog.destroy()
            
    def get_test_data(self):
        """Get the test data."""
        data = {
            "date": ITkDButils.get_db_date(),
            "properties": {},
            "results": {},
            "comments": [],
            "defects": []
        }
        self.get_test_header(data)
        self.get_list_of_channels(data)
        return data
    
    def get_test_header(self, data):
        """Get Basic test data."""
        SN = self.SN.get_text()
        operator = self.operator.get_text()
        machine = self.machine.get_text()
        batch = self.batch.get_text()

        if not SN or len(SN)==0:
            SN = dbGtkUtils.get_a_value("Module Serial Number", 
                                        "Module serial Number is missing")

        if len(operator) == 0 or len(machine) == 0 or len(batch) == 0:
            values = dbGtkUtils.get_a_list_of_values(
                "Missing Values",
                ["SN", "Operator", "Wire Bonder", "Wire Batch"],
                defaults=[SN, operator, machine, batch],
            )
            if len(values) == 4:
                SN, operator, machine, batch = values
            else:
                self.write_message("Something went wrong whilerequesting missing information.")

        data["component"] = SN
        data["properties"]["OPERATOR"] = operator
        data["properties"]["BOND_MACHINE"] = machine
        data["properties"]["BONDWIRE_BATCH"] = batch

            
    def upload_test(self, *args):
        """Upload test."""
        if self.session is None:
            self.pdb = ITkDBlogin.ITkDBlogin()
            client = self.pdb.get_client()
            if client is None:
                dbGtkUtils.complain("Could not connect to DB with provided credentials.")
                self.pdb.die()

            else:
                self.session = client
                
        defaults = {
            "institution": "IFIC",
            "runNumber": "1",
            "date":  ITkDButils.get_db_date()
        }
        skeleton = ITkDButils.get_test_skeleton(self.session, "MODULE", "MODULE_WIRE_BONDING", defaults)

        self.get_test_header(skeleton)        
        self.get_list_of_channels(skeleton)

        uploadW = UploadTest.UploadTest(self.session, payload=skeleton)
        # uploadW.run()


if __name__ == "__main__":

    win = WireBond("WireBond")
    win.connect("destroy", Gtk.main_quit)
    try:
        Gtk.main()

    except KeyboardInterrupt:
        print("Arrrgggg!!!")
