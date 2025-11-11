using System.Drawing;

namespace ControlLED
{
    public class BotonBlink : BotonBase
    {
        public BotonBlink()
        {
            Configurar("Blink", 0x03, Color.LightSkyBlue);
        }
    }
}