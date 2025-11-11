using System;
using System.Windows.Forms;
using System.Drawing;
using System.Threading.Tasks;

namespace ControlLED
{
    public partial class Form1 : Form
    {
        private ControlSerial controlSerial;
        private BotonBase[] botones;
        private bool comandoEnEjecucion = false;

        public Form1()
        {
            InitializeComponent();
            InicializarSistema();
        }

        private void InicializarSistema()
        {
            controlSerial = new ControlSerial();

            if (controlSerial.ConectarAutomatico())
            {
                CrearInterfaz();
            }
            else
            {
                MostrarError();
            }
        }

        private void CrearInterfaz()
        {
            this.Controls.Clear();

            botones = new BotonBase[]
            {
                new BotonLlenado(),
                new BotonBorrado(),
                new BotonBlink(),
                new BotonEncendido()
            };

            for (int i = 0; i < botones.Length; i++)
            {
                var boton = botones[i];
                boton.Location = new Point(50, 50 + (i * 60));
                boton.OnClickComando += async (comando) =>
                {
                    if (!comandoEnEjecucion)
                    {
                        await EjecutarComando(comando);
                    }
                };
                this.Controls.Add(boton);
            }

            // Estado de conexión
            var lblEstado = new Label();
            lblEstado.Text = $"Conectado a: {controlSerial.NombrePuerto}";
            lblEstado.Location = new Point(50, 300);
            lblEstado.Size = new Size(200, 20);
            lblEstado.ForeColor = Color.Green;
            this.Controls.Add(lblEstado);
        }

        private async Task EjecutarComando(byte comando)
        {
            if (comandoEnEjecucion) return;

            comandoEnEjecucion = true;

            // Bloquear todos los botones
            foreach (var btn in botones)
            {
                btn.Bloquear();
            }

            System.Diagnostics.Debug.WriteLine($"🎯 ENVIANDO COMANDO: 0x{comando:X2}");

            // Enviar comando
            bool confirmado = await controlSerial.EnviarComandoYEsperarConfirmacion(comando, 8);

            if (confirmado)
            {
                System.Diagnostics.Debug.WriteLine("✅ COMANDO EXITOSO");
            }
            else
            {
                System.Diagnostics.Debug.WriteLine("❌ FALLO EL COMANDO");
                await Task.Delay(2000);
            }

            // Desbloquear botones
            foreach (var btn in botones)
            {
                btn.Desbloquear();
            }
            comandoEnEjecucion = false;
        }

        private void MostrarError()
        {
            this.Controls.Clear();

            var lblError = new Label();
            lblError.Text = "No se pudo conectar al puerto serial";
            lblError.Location = new Point(50, 50);
            lblError.Size = new Size(250, 20);
            lblError.ForeColor = Color.Red;
            this.Controls.Add(lblError);

            var btnReintentar = new Button();
            btnReintentar.Text = "Reintentar Conexión";
            btnReintentar.Location = new Point(50, 80);
            btnReintentar.Size = new Size(150, 30);
            btnReintentar.Click += (s, e) =>
            {
                this.Controls.Clear();
                InicializarSistema();
            };
            this.Controls.Add(btnReintentar);
        }

        protected override void OnFormClosing(FormClosingEventArgs e)
        {
            controlSerial?.Desconectar();
            base.OnFormClosing(e);
        }
    }
}