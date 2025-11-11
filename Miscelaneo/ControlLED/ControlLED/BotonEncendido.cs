using System.Drawing;

namespace ControlLED
{
    public class BotonEncendido : BotonBase
    {
        public BotonEncendido()
        {
            Configurar("Encendido Secuencial", 0x04, Color.LightGreen);
        }
    }
}