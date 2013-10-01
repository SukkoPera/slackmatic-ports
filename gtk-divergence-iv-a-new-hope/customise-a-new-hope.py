#!/usr/bin/env python
_app_name = "Orta Configurator"
_version = "0.1"
_bugs = "Please report all bugs to <valiant.wing@gmail.com>."
_config_header = """#
# Orta Config File
#
#
"""

import pygtk
pygtk.require("2.0")
import gtk
import sys
import os
import urllib2
import shutil
import subprocess


_filename = os.path.basename(sys.argv[0])
_cust_basedir = "/usr/share/gtk-2.0/a-new-hope-customiser"
_themedir = "/usr/share/themes/A-New-Hope"

# GLOBALS
panel_type = 1
tab_type = 1
scrollbar_type = 1
nautilus_type = 1
menu_type = 1

gtk_breadcrumbs_check = False


def copy (src, dst):
	global _themedir
	
	# All src files are relative to the theme directory
	src = os.path.join (_themedir, src)
	
	# All dst files are relative to the theme directory (can't this be the user's home directory???)
	dst = os.path.join (_themedir, dst)
	
	#print "Copying %s to %s" % (src, dst)
	#shutil.copyfile (src, dst)
	#copy ("gtk-2.0/Styles/RES/panel-sunken.rc", "gtk-2.0/Styles/panel.rc")
	

class OrtaConfigurator:

# PANEL TAB
	def on_default_panel_toggled(self, widget, data=None):
		global panel_type
		panel_type = 1

	def on_raised_panel_toggled(self, widget, data=None):
		global panel_type
		panel_type = 2

	def on_light_panel_toggled(self, widget, data=None):
		global panel_type
		panel_type = 3

# TABS TAB
	def on_tabs_default_toggled(self, widget, data=None):
		global tab_type
		tab_type = 1

	def on_tabs_dark_toggled(self, widget, data=None):
		global tab_type
		tab_type = 2


# SCROLLBARS TAB
	def on_scrollbars_default_toggled(self, widget, data=None):
		global scrollbar_type
		scrollbar_type = 1

	def on_scrollbars_dark_toggled(self, widget, data=None):
		global scrollbar_type
		scrollbar_type = 2

# NAUTILUS TAB
	def on_nautilus_default_toggled(self, widget, data=None):
		global nautilus_type
		nautilus_type = 1

	def on_nautilus_tesb_toggled(self, widget, data=None):
		global nautilus_type
		nautilus_type = 2

	def on_nautilus_rotj_toggled(self, widget, data=None):
		global nautilus_type
		nautilus_type = 3

	def on_gtk_breadcrumbs_checked(self, widget, data=None):
		global gtk_breadcrumbs_check
		if gtk_breadcrumbs_check :
			gtk_breadcrumbs_check = False
		else :
			gtk_breadcrumbs_check = True

# MENUS TAB
	def on_menu_default_toggled(self, widget, data=None):
		global menu_type
		menu_type = 1

	def on_menu_squared_toggled(self, widget, data=None):
		global menu_type
		menu_type = 2

	def on_menu_raised_toggled(self, widget, data=None):
		global menu_type
		menu_type = 3




# SAVE BUTTON CLICKED		
	def on_save_clicked(self, widget, data=None):
	# PANEL TYPE
		if panel_type == 1 :
			copy ("gtk-2.0/Styles/RES/panel-sunken.rc", "gtk-2.0/Styles/panel.rc")
		elif panel_type == 2 :
			copy ("gtk-2.0/Styles/RES/panel-raised.rc", "gtk-2.0/Styles/panel.rc")
		elif panel_type == 3 :
			copy ("gtk-2.0/Styles/RES/panel-light.rc", "gtk-2.0/Styles/panel.rc")
	# TAB TYPE
		if tab_type == 1 :
			copy ("gtk-2.0/Styles/RES/notebook-light.rc", "gtk-2.0/Styles/notebook.rc")
		elif tab_type == 2 :
			copy ("gtk-2.0/Styles/RES/notebook-dark.rc", "gtk-2.0/Styles/notebook.rc")

	# SCROLLBAR TYPE
		if scrollbar_type == 1 :
			copy ("gtk-2.0/Styles/RES/scrollbar-light.rc", "gtk-2.0/Styles/scrollbar.rc")
		elif scrollbar_type == 2 :
			copy ("gtk-2.0/Styles/RES/scrollbar-dark.rc", "gtk-2.0/Styles/scrollbar.rc")

	# NAUTILUS TYPE
		if nautilus_type == 1 :
			copy ("gtk-2.0/Styles/RES/toolbar-dark.rc", "gtk-2.0/Styles/toolbar.rc")
			copy ("gtk-2.0/Styles/RES/nautilus-ANH.rc", "gtk-2.0/Styles/nautilus.rc")
			copy ("gtk-2.0/Styles/RES/breadcrumbs-dark.rc", "gtk-2.0/Styles/breadcrumbs.rc")
		elif nautilus_type == 2 :
			copy ("gtk-2.0/Styles/RES/toolbar-dark.rc", "gtk-2.0/Styles/toolbar.rc")
			copy ("gtk-2.0/Styles/RES/nautilus-TESB.rc", "gtk-2.0/Styles/nautilus.rc")
			copy ("gtk-2.0/Styles/RES/breadcrumbs-dark.rc", "gtk-2.0/Styles/breadcrumbs.rc")
		elif nautilus_type == 3 :
			copy ("gtk-2.0/Styles/RES/toolbar-light.rc", "gtk-2.0/Styles/toolbar.rc")
			copy ("gtk-2.0/Styles/RES/nautilus-ROTJ.rc", "gtk-2.0/Styles/nautilus.rc")
			copy ("gtk-2.0/Styles/RES/breadcrumbs-light.rc", "gtk-2.0/Styles/breadcrumbs.rc")

	# ELEMENTARY OR GTK BREADCRUMBS CHECK
		if gtk_breadcrumbs_check :
			copy ("gtk-2.0/Styles/RES/null.rc", "gtk-2.0/Styles/breadcrumbs.rc")

	# MENU TYPE
		if menu_type == 1 :
			copy ("gtk-2.0/Styles/RES/menu-round.rc", "gtk-2.0/Styles/menu.rc")
		elif menu_type == 2 :
			copy ("gtk-2.0/Styles/RES/menu-lessround.rc", "gtk-2.0/Styles/menu.rc")
		elif menu_type == 3 :
			copy ("gtk-2.0/Styles/RES/menu-raised.rc", "gtk-2.0/Styles/menu.rc")

		save_dialog = self.builder.get_object("SettingsSavedDialog")
		save_dialog.show()

# SAVE OK DIALOG
	def on_settings_saved_ok_clicked(self, widget, data=None):
		save_dialog = self.builder.get_object("SettingsSavedDialog")
		save_dialog.hide()
		try:
			os.system("killall gnome-appearance-properties")
			subprocess.Popen('gnome-appearance-properties')
		except StandardError :
			no_gnome_dialog = self.builder.get_object("GnomeNotFoundDialog")
			no_gnome_dialog.show()

	
	def on_mainWindow_destroy(self, widget, data=None):
		gtk.main_quit()
    
	def on_quit_clicked(self, widget, data=None):
		gtk.main_quit()
 
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file(os.path.join(_cust_basedir, "ANewHopeConfigurator.ui"))
		self.builder.connect_signals(self)
		self.window = self.builder.get_object("mainWindow")
		self.window.show()
    
	def main_loop(self):
		gtk.main()
		return 0

def main():
    configurator = OrtaConfigurator()
    configurator.main_loop()
    
if __name__ == "__main__":
    main()
