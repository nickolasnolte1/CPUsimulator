# CPUsimulator
Proyecto 1 Programación de Dispositivos Electrónicos

En el presente proyecto se llevó a cabo un simulador de CPU (control process unit). La simulación es de un 4-bit CPU que cuenta con las funciones de Control Unit (CU), un Arithmetic Logic Unit (ALU), 4 Registers (más unos extra), RAM de 16 bytes y un Clock.

El simulador puede leer un programa de un archivo ".cpufm" que cuenta con una programación en código máquina. Todas las instrucciones que se le den al CPU tendrán que tener el formato string "1100 0011". Aún así, puede llevarse a cabo por medio de instrucciones mnemonic (0001 = LOAD_R0).

El proceso de Fetch-Decode-Execute se realiza de la manera más rápida posible. Cuenta con un reloj de 0.5 determinado que indica la frecuencia del instruction-cycle. 

Se dividió el programa por módulos y clases con sus respectivos atributos y métodos. Cada uno de ellos haciendo posible la simulacion de cada una de las funciones del CPU. 
