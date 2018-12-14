using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace NavisPythonShell.NpsRuntime
{
    public interface IRpsConfig
    {
        /// <summary>
        /// Returns a list of string variables that the Runtime will add to
        /// the scripts scope under "__vars__".
        /// 
        /// In NavisPythonShell, these are read from the NavisPythonShell.xml file.
        /// </summary>
        IDictionary<string, string> GetVariables();

        /// <summary>
        /// Returns a list of paths to add to the python engine search paths.
        /// 
        /// In NavisPythonShell, these are read from the NavisPythonShell.xml file.
        /// </summary>
        IEnumerable<string> GetSearchPaths();
    }
}
