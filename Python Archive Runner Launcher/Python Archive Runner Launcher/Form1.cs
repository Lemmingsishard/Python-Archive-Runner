using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;

namespace Python_Archive_Runner_Launcher
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void CLI_Button_Click(object sender, EventArgs e)
        {
            //this drove me crazy
            ProcessStartInfo cmd = new ProcessStartInfo();
            cmd.FileName = "python.exe";
            cmd.WindowStyle = ProcessWindowStyle.Normal;
            cmd.Arguments = @"Python_Archive_Runner.py";
            cmd.UseShellExecute = true;
            Process.Start(cmd);
        }

        private void GUI_version_Click(object sender, EventArgs e)
        {
            ProcessStartInfo cmd = new ProcessStartInfo();
            cmd.FileName = "python.exe";
            cmd.WindowStyle = ProcessWindowStyle.Hidden;
            cmd.Arguments = @"Python_Archive_Runnertk.pyw";
            cmd.UseShellExecute = true;
            Process.Start(cmd);
        }
    }
}
