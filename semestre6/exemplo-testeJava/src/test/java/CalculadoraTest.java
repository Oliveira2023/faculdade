import org.example.Calculadora;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class CalculadoraTest {
    @Test
    public void testSoma() {
        Calculadora calculadora = new Calculadora();

        assertEquals(4, calculadora.soma(2, 2), 0);
    }

}
