using System;
using System.IO.Ports;
using System.Threading.Tasks;

namespace ControlLED
{
    public class ControlSerial
    {
        private SerialPort puerto;

        public bool Conectado => puerto?.IsOpen ?? false;
        public string NombrePuerto => puerto?.PortName ?? "No conectado";
        public string[] PuertosDisponibles => SerialPort.GetPortNames();

        public ControlSerial()
        {
        }

        public SerialPort GetSerialPort()
        {
            return puerto;
        }

        public bool Conectar(string nombrePuerto = null, int baudRate = 9600)
        {
            try
            {
                if (string.IsNullOrEmpty(nombrePuerto))
                {
                    var puertos = PuertosDisponibles;
                    if (puertos.Length == 0) return false;
                    nombrePuerto = puertos[0];
                }

                if (puerto?.IsOpen == true)
                    puerto.Close();

                puerto = new SerialPort(nombrePuerto, baudRate, Parity.None, 8, StopBits.One);
                puerto.ReadTimeout = 5000;
                puerto.WriteTimeout = 1000;
                puerto.Open();

                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }

        public bool ConectarAutomatico()
        {
            var puertos = PuertosDisponibles;
            foreach (string port in puertos)
            {
                if (Conectar(port)) return true;
            }
            return false;
        }

        public async Task<bool> EnviarComandoYEsperarConfirmacion(byte comando, int timeoutSegundos = 10)
        {
            if (!Conectado) return false;

            try
            {
                System.Diagnostics.Debug.WriteLine($"🚀 ENVIANDO COMANDO: 0x{comando:X2}");

                puerto.DiscardInBuffer();
                byte[] buffer = new byte[] { comando };
                puerto.Write(buffer, 0, 1);

                // ✅ ESPERAR antes de verificar (dar tiempo al Pi Pico)
                await Task.Delay(100);

                DateTime inicio = DateTime.Now;

                while ((DateTime.Now - inicio).TotalSeconds < timeoutSegundos)
                {
                    if (puerto.BytesToRead > 0)
                    {
                        byte respuesta = (byte)puerto.ReadByte();
                        System.Diagnostics.Debug.WriteLine($"📥 RESPUESTA RECIBIDA: 0x{respuesta:X2}");

                        if (respuesta == 0xFF)
                        {
                            System.Diagnostics.Debug.WriteLine("✅ CONFIRMACION 0xFF RECIBIDA");
                            return true;
                        }
                    }
                    await Task.Delay(50);
                }

                System.Diagnostics.Debug.WriteLine("❌ TIMEOUT - NO SE RECIBIO 0xFF");
                return false;
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine($"💥 ERROR: {ex.Message}");
                return false;
            }
        }
        public void EnviarByteDirecto(byte comando)
        {
            if (!Conectado) return;

            try
            {
                System.Diagnostics.Debug.WriteLine($"🔴🔄 ENVIANDO BYTE DIRECTO: 0x{comando:X2}");
                puerto.DiscardInBuffer();
                byte[] buffer = new byte[] { comando };
                puerto.Write(buffer, 0, 1);
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine($"🔴💥 ERROR DIRECTO: {ex.Message}");
            }
        }

        public void Desconectar()
        {
            if (puerto != null && puerto.IsOpen)
            {
                puerto.Close();
            }
        }
    }
}