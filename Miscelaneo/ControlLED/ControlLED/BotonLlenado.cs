using System.Drawing;

namespace ControlLED
{
    public class BotonLlenado : BotonBase
    {
        public BotonLlenado()
        {
            Configurar("Llenado Secuencial", 0x01, Color.LightBlue);
        }
    }
}