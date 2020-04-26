using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Basic_Calculator
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
           
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            lb_ANS.Visible = false;
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            lb_ANS.Visible = true;
            lb_ANS.Text = Convert.ToString(Convert.ToDecimal(textBox1.Text) + Convert.ToDecimal(textBox2.Text));
        }

        private void subtract_Click(object sender, EventArgs e)
        {
            lb_ANS.Visible = true;
            lb_ANS.Text = Convert.ToString(Convert.ToDecimal(textBox1.Text) - Convert.ToDecimal(textBox2.Text));
        }

        private void multiply_Click(object sender, EventArgs e)
        {
            lb_ANS.Visible = true;
            lb_ANS.Text = Convert.ToString(Convert.ToDecimal(textBox1.Text) * Convert.ToDecimal(textBox2.Text));
        }

        private void divide_Click(object sender, EventArgs e)
        {
            lb_ANS.Visible = true;
            lb_ANS.Text = Convert.ToString(Convert.ToDecimal(textBox1.Text) / Convert.ToDecimal(textBox2.Text));
        }
    }
}
