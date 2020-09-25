# CPUsimulator
Proyecto 1 Programación de Dispositivos Electrónicos

En el presente proyecto se llevó a cabo un simulador de CPU (control process unit). La simulación es de un 4-bit CPU que cuenta con las funciones de Control Unit (CU), un Arithmetic Logic Unit (ALU), 4 Registers (más unos extra), RAM de 16 bytes y un Clock.

El simulador puede leer un programa de un archivo ".cpufm" que cuenta con una programación en código máquina. Todas las instrucciones que se le den al CPU tendrán que tener el formato string "1100 0011". Aún así, puede llevarse a cabo por medio de instrucciones mnemonic (0001 = LOAD_R0).

El proceso de Fetch-Decode-Execute se realiza de la manera más rápida posible. Cuenta con un reloj de 0.5 determinado que indica la frecuencia del instruction-cycle. 

Se dividió el programa por módulos y clases con sus respectivos atributos y métodos. Cada uno de ellos haciendo posible la simulacion de cada una de las funciones del CPU. 
 
 

# Información componentes CPU
CU: La unidad de control es responsable de buscar el conjunto de instrucciones, controlando el flujo de datos en toda el CPU, también controla el tiempo de cada operación y la interacción con dispositivos periféricos.

ALU: Unidad Aritmética Lógica, es un circuito electrónico digital responsable de (dependiendo del procesador) hacer todas las operaciones aritméticas como (pero No limitado a):
● Sumar
● Restar
● Restar con acarreo
● Complemento a uno
● Complemento a dos
● And
● Or
● Operaciones de cambio de bit
● > <<>> =

Registros: Una parte importante de la memoria, en la que que el CU y el ALU pueden almacenar temporalmente los datos; un registro importante es el contador del programa que realiza un seguimiento de donde la CPU está leyendo del conjunto de instrucciones.
● Registro de instrucciones (instrucción actual cargada)
● Registro de dirección de instrucción (contador de programa)

RAM: Random Acces Memory
● Datos
● Instrucciones

Reloj: Es el encargado de controlar el ciclo de búsqueda-decodificación-ejecución (fetch-decode-execute).
