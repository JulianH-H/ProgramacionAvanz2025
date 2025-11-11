using System;
using System.IO.Ports;
using System.Windows.Forms;
using System.Drawing;

namespace ControlLED
{
    public class SimpleSerialMonitor : Form
    {
        private SerialPort puerto;
        private ListBox lstMessages;
        private Button btnClear;
        private int ffCount = 0;

        public SimpleSerialMonitor(SerialPort serialPort)
        {
            puerto = serialPort;
            InitializeComponent();

            if (puerto != null)
            {
                puerto.DataReceived += Puerto_DataReceived;
            }
        }

        private void InitializeComponent()
        {
            this.Text = "Debug Serial - Ver 0xFF";
            this.Size = new Size(400, 300);
            this.StartPosition = FormStartPosition.CenterScreen;

            // ListBox para mensajes
            lstMessages = new ListBox();
            lstMessages.Dock = DockStyle.Fill;
            lstMessages.Font = new Font("Consolas", 9);
            this.Controls.Add(lstMessages);

            // Panel inferior
            var panel = new Panel();
            panel.Dock = DockStyle.Bottom;
            panel.Height = 30;
            this.Controls.Add(panel);

            // Botón limpiar
            btnClear = new Button();
            btnClear.Text = "Limpiar";
            btnClear.Location = new Point(10, 3);
            btnClear.Size = new Size(80, 24);
            btnClear.Click += (s, e) => {
                lstMessages.Items.Clear();
                ffCount = 0;
                UpdateTitle();
            };
            panel.Controls.Add(btnClear);

            // Etiqueta de estado
            var lblStatus = new Label();
            lblStatus.Text = puerto != null ? $"Puerto: {puerto.PortName}" : "Puerto no disponible";
            lblStatus.Location = new Point(100, 6);
            lblStatus.Size = new Size(200, 20);
            lblStatus.ForeColor = Color.Blue;
            panel.Controls.Add(lblStatus);

            UpdateTitle();
        }

        private void Puerto_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {
            try
            {
                while (puerto.BytesToRead > 0)
                {
                    int byteRecibido = puerto.ReadByte();
                    string timestamp = DateTime.Now.ToString("HH:mm:ss.fff");

                    string mensaje = byteRecibido == 0xFF
                        ? $"[{timestamp}] ✅ 0xFF RECIBIDO (Confirmación #{++ffCount})"
                        : $"[{timestamp}] 📥 0x{byteRecibido:X2}";

                    this.Invoke(new Action(() =>
                    {
                        lstMessages.Items.Add(mensaje);
                        lstMessages.TopIndex = lstMessages.Items.Count - 1;
                        UpdateTitle();
                    }));
                }
            }
            catch (Exception ex)
            {
                this.Invoke(new Action(() =>
                {
                    lstMessages.Items.Add($"[ERROR] {ex.Message}");
                }));
            }
        }

        private void UpdateTitle()
        {
            this.Invoke(new Action(() =>
            {
                this.Text = $"Debug Serial - 0xFF: {ffCount} recibidos";
            }));
        }

        protected override void OnFormClosing(FormClosingEventArgs e)
        {
            if (puerto != null)
            {
                puerto.DataReceived -= Puerto_DataReceived;
            }
            base.OnFormClosing(e);
        }
    }
}