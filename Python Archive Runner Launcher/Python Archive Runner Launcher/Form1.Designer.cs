namespace Python_Archive_Runner_Launcher
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.CLI_Button = new System.Windows.Forms.Button();
            this.GUI_version = new System.Windows.Forms.Button();
            this.textbox = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // CLI_Button
            // 
            this.CLI_Button.Font = new System.Drawing.Font("Pivot Classic", 16F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.CLI_Button.Location = new System.Drawing.Point(35, 176);
            this.CLI_Button.Name = "CLI_Button";
            this.CLI_Button.Size = new System.Drawing.Size(267, 140);
            this.CLI_Button.TabIndex = 0;
            this.CLI_Button.Text = "Use CLI";
            this.CLI_Button.UseVisualStyleBackColor = true;
            this.CLI_Button.Click += new System.EventHandler(this.CLI_Button_Click);
            // 
            // GUI_version
            // 
            this.GUI_version.Font = new System.Drawing.Font("Pivot Classic", 16F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.GUI_version.Location = new System.Drawing.Point(486, 176);
            this.GUI_version.Name = "GUI_version";
            this.GUI_version.Size = new System.Drawing.Size(283, 140);
            this.GUI_version.TabIndex = 1;
            this.GUI_version.Text = "Use GUI";
            this.GUI_version.UseVisualStyleBackColor = true;
            this.GUI_version.Click += new System.EventHandler(this.GUI_version_Click);
            // 
            // textbox
            // 
            this.textbox.AutoSize = true;
            this.textbox.Font = new System.Drawing.Font("Pivot Classic", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textbox.Location = new System.Drawing.Point(5, 28);
            this.textbox.Name = "textbox";
            this.textbox.Size = new System.Drawing.Size(817, 92);
            this.textbox.TabIndex = 2;
            this.textbox.Text = "Which version of Python Archive Runner \n          would you like to use";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.textbox);
            this.Controls.Add(this.GUI_version);
            this.Controls.Add(this.CLI_Button);
            this.Name = "Form1";
            this.Text = "Python Archive Runner";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button CLI_Button;
        private System.Windows.Forms.Button GUI_version;
        private System.Windows.Forms.Label textbox;
    }
}

