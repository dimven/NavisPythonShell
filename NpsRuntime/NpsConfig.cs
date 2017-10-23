using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml.Linq;

namespace NavisPythonShell.NpsRuntime
{
    /// <summary>
    /// Provides access functions to those parts of the NavisPythonShell.xml file
    /// that are also used in RpsAddin deployments.
    /// </summary>
    public class NpsConfig: IRpsConfig
    {
        /// <summary>
        /// The full path to the settings file used (e.g. %APPDATA%\NavisPythonShell2017\NavisPythonShell.xml)
        /// </summary>
        private readonly string _settingsPath;
        private readonly XDocument _settings;
        private readonly SettingsDictionary _dict;

        public NpsConfig(string settingsFilePath)
        {
            _settingsPath = settingsFilePath;
            _settings = XDocument.Load(_settingsPath);
            _dict = new SettingsDictionary(_settingsPath);
        }

        /// <summary>
        /// Returns a list of search paths to be added to python interpreter engines.
        /// </summary>
        public IEnumerable<string> GetSearchPaths()
        {
            foreach (var searchPathNode in _settings.Root.Descendants("SearchPath"))
            {
                yield return searchPathNode.Attribute("name").Value;
            }
            yield return System.IO.Path.GetDirectoryName(_settingsPath);
        }

        /// <summary>
        /// Returns the list of variables to be included with the scope in NavisPythonShell scripts.
        /// </summary>
        public IDictionary<string, string> GetVariables()
        {
            return _dict;
        }               
    }
}
