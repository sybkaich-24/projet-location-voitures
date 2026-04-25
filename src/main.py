from controleur.application import Application

def main():
    print("Démarrage de l'application de location de voitures...")
    # Instance de l'application
    app = Application()
    # Démarrage de l'application
    app.run()

if __name__ == "__main__":
    main()