using System;
using System.Windows.Forms;

namespace NavisPythonShell.NpsRuntime
{
    public partial class ScriptOutput : Form
    {
        public ScriptOutput()
        {
            InitializeComponent();
            txtStdOut.Text = "";            
        }
    }
}
