using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Diagnostics;
using Microsoft.Scripting;
using System.Threading;
using System.Windows.Threading;
using NavisPythonShell.NpsRuntime;
using Forms = System.Windows.Forms;
using Autodesk.Navisworks.Api;
using Autodesk.Navisworks.Api.Plugins;

namespace NavisPythonShell
{
    /// <summary>
    /// Start an interactive shell in a modal window.
    /// </summary>

    [PluginAttribute("NavisPythonShell.IronPythonConsoleCommand",                   
                     "ACOM",
                     ToolTip = "NavisPythonShell IronPython Console",
                     DisplayName = "Run NPS")]
    [AddInPluginAttribute(AddInLocation.AddIn,
        				  Icon = "Icons\\Python-16.ico",
        				  LargeIcon = "Icons\\Python-32.ico", 
        				  LoadForCanExecute = true)]
    public class IronPythonConsoleCommand : AddInPlugin
    {
        /// <summary>
        /// Open a window to let the user enter python code.
        /// </summary>
        /// <returns></returns>
        public override int Execute(params string[] parameters)
        {            
        	//load the application
        	if (!NavisPythonShellApplication.applicationLoaded)
        	{
        		NavisPythonShellApplication.OnLoaded();
        	}
        	
            var gui = new IronPythonConsole();
            gui.consoleControl.WithConsoleHost((host) =>
            {
                // now that the console is created and initialized, the script scope should
                // be accessible...
                new ScriptExecutor(NavisPythonShellApplication.GetConfig() )
                    .SetupEnvironment(host.Engine, host.Console.ScriptScope);

                host.Console.ScriptScope.SetVariable("__window__", gui);

                // run the initscript
                var initScript = NavisPythonShellApplication.GetInitScript();
                if (initScript != null)
                {
                    try
                    {
                    	var scriptSource = host.Engine.CreateScriptSourceFromString(initScript, SourceCodeKind.Statements);
                    	scriptSource.Execute(host.Console.ScriptScope);
                    }
                    catch (Exception ex)
                    {
                    	Forms.MessageBox.Show(ex.ToString(), "Something went horribly wrong!");
                    }
                }                
            });

            var dispatcher = Dispatcher.FromThread(Thread.CurrentThread);
            gui.consoleControl.WithConsoleHost((host) =>
            {                
                host.Console.SetCommandDispatcher((command) =>
                {
                    if (command != null)
                    {
                        // Slightly involved form to enable keyboard interrupt to work.
                        var executing = true;
                        var operation = dispatcher.BeginInvoke(DispatcherPriority.Normal, command);
                        while (executing)
                        {
                            if (operation.Status != DispatcherOperationStatus.Completed)
                                operation.Wait(TimeSpan.FromSeconds(1));
                            if (operation.Status == DispatcherOperationStatus.Completed)
                                executing = false;
                        }
                    }                 
                });
                host.Editor.SetCompletionDispatcher((command) =>
                {
                    var executing = true;
                    var operation = dispatcher.BeginInvoke(DispatcherPriority.Normal, command);
                    while (executing)
                    {
                        if (operation.Status != DispatcherOperationStatus.Completed)
                            operation.Wait(TimeSpan.FromSeconds(1));
                        if (operation.Status == DispatcherOperationStatus.Completed)
                            executing = false;
                    }
                });
            });
            gui.ShowDialog();
            return 0;
        }
    }    
}
