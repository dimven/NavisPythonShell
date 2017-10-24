using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using Autodesk.Navisworks.Api;
using Autodesk.Navisworks.Api.Plugins;

namespace NavisPythonShell
{
    /// <summary>
    /// Open the configuration dialog.
    /// </summary>

    [PluginAttribute("NavisPythonShell.ConfigureCommand",                   
                     "ACOM",
                     ToolTip = "NPS configuration window",
                     DisplayName = "Configure NPS")]
    [AddInPluginAttribute(AddInLocation.AddIn,
        				  Icon = "Icons\\Settings-16.ico",
        				  LargeIcon = "Icons\\Settings-32.ico", 
        				  LoadForCanExecute = true)]
    class ConfigureCommand : AddInPlugin
    {
        public override int Execute(params string[] parameters)
        {
            //load the application
        	if (!NavisPythonShellApplication.applicationLoaded)
        	{
        		NavisPythonShellApplication.OnLoaded();
        	}
        	
        	var dialog = new ConfigureCommandsForm();
            dialog.ShowDialog();

            //MessageBox.Show("Restart Navisworks to see changes to the commands in the Ribbon", "Configure NavisPythonShell", MessageBoxButtons.OK, MessageBoxIcon.Information);

            return 0;
        }
    }
}
