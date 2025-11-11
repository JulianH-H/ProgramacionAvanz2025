using System.Drawing;

namespace ControlLED
{
    public class BotonBorrado : BotonBase
    {
        public BotonBorrado()
        {
            Configurar("Borrado Secuencial", 0x02, Color.LightCoral);
        }
    }
}