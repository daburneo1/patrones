using System;

namespace DB.DesignPatterns.Command.Conceptual
{
    // La interfaz Command declara un método para ejecutar un comando
    public interface ICommand
    {
        void Execute();
    }

    // Algunos comandos pueden implementar operaciones simples por sí mismos
    class SimpleCommand : ICommand
    {
        private string _payload = string.Empty;

        public SimpleCommand(string payload)
        {
            this._payload = payload;
        }

        public void Execute()
        {
            Console.WriteLine($"SimpleCommand: Mira, puedo hacer cosas simples como imprimir ({this._payload})");
        }
    }

    // Sin embargo, algunos comandos pueden delegar operaciones más complejas a otros
    // objetos llamados "receptores"
    class ComplexCommand : ICommand
    {
        private Receiver _receiver;

        // Datos de contexto, necesarios para iniciar los métodos del receptor
        private string _a;

        private string _b;

        // Los comandos complejos pueden aceptar uno o varios objetos receptores junto
        // con cualquier dato de contexto a través del constructor
        public ComplexCommand(Receiver receiver, string a, string b)
        {
            this._receiver = receiver;
            this._a = a;
            this._b = b;
        }

        // Los comandos pueden delegar a cualquier método de un receptor
        public void Execute()
        {
            Console.WriteLine("ComplexCommand: Las cosas complejas deben ser realizadas por un objeto Receiver.");
            this._receiver.DoSomething(this._a);
            this._receiver.DoSomethingElse(this._b);
        }
    }

    // La clase Receiver puede realizar todo tipo de operaciones asociadas a la realización
    // de una solicitud. Cualquier clase puede servir como Receiver
    class Receiver
    {
        public void DoSomething(string a)
        {
            Console.WriteLine($"Receiver: Trabajando en ({a}.)");
        }

        public void DoSomethingElse(string b)
        {
            Console.WriteLine($"Receiver: También trabajando en ({b}.)");
        }
    }

    // Invoker está asociado a uno o varios comandos
    class Invoker
    {
        private ICommand _onStart;

        private ICommand _onFinish;

        // Initialize commands.
        public void SetOnStart(ICommand command)
        {
            this._onStart = command;
        }

        public void SetOnFinish(ICommand command)
        {
            this._onFinish = command;
        }

        // Invoker no depende de clases concretas, comandos o receptores. Invoker pasa 
        // una solicitud a un receptor indirectamente, ejecutando un comando

        public void DoSomethingImportant()
        {
            Console.WriteLine("Invoker: Alguien quiere hacer algo antes de empezar?");
            if (this._onStart is ICommand)
            {
                this._onStart.Execute();
            }
            
            Console.WriteLine("Invoker: ...trabajando en algo muy importante...");
            
            Console.WriteLine("Invoker: Alguien desea algo después de que termine?");
            if (this._onFinish is ICommand)
            {
                this._onFinish.Execute();
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // El cliente puede parametrizar un Invoker con cualquier comando
            Invoker invoker = new Invoker();
            invoker.SetOnStart(new SimpleCommand("Trabajando!!!"));
            Receiver receiver = new Receiver();
            invoker.SetOnFinish(new ComplexCommand(receiver, "Envia un email", "Guarda un reporte"));

            invoker.DoSomethingImportant();
        }
    }
}