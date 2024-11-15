
import math
import random 
from colorama import Fore, Style, init
# Inizializza colorama per i colori
init(autoreset=True)
def ask_for_number(prompt):
    while True:
        try:
            return float(input(Fore.YELLOW + prompt))
        except ValueError:
            print(Fore.RED + "Ehm, quello non sembra proprio un numero! Riprova, dopo aver studiato in modo serio.")
# Altre funzioni come calculate_square, calculate_circle, ecc.
def guess_the_shape():
    print("Entrato in guess_the_shape()")
    # Il resto del codice della funzione...
#Chiamata finale per avviare il programma
print("Il programma è avviato!")
print("Sto per chiamare guess_the_shape()")
guess_the_shape()          
def calculate_square():
    side = ask_for_number("Ah... Un quadrato! Inserisci la lunghezza del lato: ")
    perimeter = 4 * side
    area = side ** 2
    print(Fore.CYAN + f"Pensavi fossi stupida... Sorpresa! Il perimetro del quadrato è {perimeter} e l'area è {area}. Quanto sono brava!")
def calculate_circle():
    radius = ask_for_number("Un cerchio perfetto... Come me! Inserisci il raggio: ")
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    print(Fore.GREEN + f"E voilà, le jeux son fe! La circonferenza è {circumference:.2f} e l'area è {area:.2f}. Che figata! Sono troppo intelligente!")
def calculate_rectangle():
    base = ask_for_number("Un rettangolo?! Che noia... Va beh! Inserisci la base: ")
    height = ask_for_number("Ora l'altezza: ")
    perimeter = 2 * (base + height)
    area = base * height
    print(Fore.MAGENTA + f"Eccoti accontentata! Il perimetro è {perimeter} e l'area è {area}. Non sarai mai alla mia altezza...")
def calculate_triangle():
    side1 = ask_for_number("Il triangolo delle bermuda! Inserisci il primo lato: ")
    side2 = ask_for_number("Ora il secondo lato: ")
    side3 = ask_for_number("Quanta pazienza... per carità, inserisci il terzo lato: ")
    perimeter = side1 + side2 + side3
    s = perimeter / 2 # semiperimetro
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    print(Fore.BLUE + f"Ci voleva tanto?! Il perimetro è {perimeter} e l'area è {area:.2f}. Sono proprio lodevole! No?!")
def playful_intro(): 
    phrases = [
            Fore.YELLOW + "Buon pomeriggio, poco acuto esploratore della geometria! Pronto a calcolare?",
            Fore.GREEN + "Buondì (non la merendina)! Oggi sarà un viaggio tra forme e numeri. Datti una mossa... Iniziamo!",
            Fore.CYAN + "Benvenuto! Io, in confronto a te sono il genio della geometria. Vuoi mettermi alla prova con qualche calcolo?"
    ]
    print(random.choice(phrases) + Style.RESET_ALL)
def guess_the_shape():
    shapes = {
        "1": ("quadrato", calculate_square),
        "2": ("cechio", calculate_circle),
        "3": ("rettangolo", calculate_rectangle),
        "4": ("triangolo", calculate_triangle)
    }
    while True:
        playful_intro()
        print(Fore.LIGHTBLUE_EX + "\nEcco le mie capacità magiche! Indovina la tua figura geometrica preferita:")
        print("1. È perfettamente quadrata.")
        print("2. È rotonda e infinita.")
        print("3. Ha due lati lunghi e due corti.")
        print("4. Ha tre lati e un cuore misterioso.")
        print("5. Uscita (se hai fifa dei calcoli magici! Patetico Babbano...)")
        choice = input(Fore.YELLOW + "Allora, che forma scegli? Inserisci il numero: ")
        if choice in shapes:
            print(Fore.LIGHTMAGENTA_EX + f"\nHmmm... difficile, molto difficile... coraggio da vendere, vedo. Hai scelto un {shapes[choice][0]}. Preparati alla magia!")
            shapes[choice][1]() # Chiama la funzione corrispondente
        elif choice == '5':
            print(Fore.RED + "Oh, dove credi di andare? Stai già scappando?! Ti voglio indietro quanto prima per altre magie!")
            break
        else:
            print(Fore.RED + "Ohioioi che disdetta, pensaci su non c'è fretta! Scelta non valida. Riprova, giovane babbano.")

calculate_square()
calculate_circle()
calculate_rectangle()
calculate_triangle()