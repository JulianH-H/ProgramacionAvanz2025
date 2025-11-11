using System;
using System.Drawing;
using System.Windows.Forms;
using System.Threading.Tasks;

namespace ControlLED
{
    public class BotonBase : Button
    {
        public byte Comando { get; protected set; }
        public string Descripcion { get; protected set; }
        
        // Evento async
        public event Func<byte, Task> OnClickComando;

        public BotonBase()
        {
            this.Font = new Font("Segoe UI", 10, FontStyle.Bold);
            this.Size = new Size(150, 40);
            this.BackColor = Color.LightGray;
            this.ForeColor = Color.Black;
            this.Click += async (s, e) => 
            {
                if (OnClickComando != null)
                    await OnClickComando(Comando);
            };
        }

        protected void Configurar(string texto, byte comando, Color color)
        {
            this.Text = texto;
            this.Comando = comando;
            this.BackColor = color;
            this.Descripcion = texto;
        }

        public void Bloquear()
        {
            this.Enabled = false;
            this.BackColor = Color.Gray;
            this.Text = $"{Descripcion}...";
        }

        public void Desbloquear()
        {
            this.Enabled = true;
            if (this is BotonLlenado) this.BackColor = Color.LightBlue;
            else if (this is BotonBorrado) this.BackColor = Color.LightCoral;
            else if (this is BotonBlink) this.BackColor = Color.LightSkyBlue;
            else if (this is BotonEncendido) this.BackColor = Color.LightGreen;
            else this.BackColor = Color.LightGray;
            
            this.Text = Descripcion;
        }
    }
}