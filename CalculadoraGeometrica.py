print("Bienvenido a la calculadora Geometrica")
Continuar = "s"

def valor_positivo(mensaje, limite=None):
    try:
        val = float(input(mensaje))
        if val <= 0:
            print("Error: Solo se permiten números positivos.")
            return valor_positivo(mensaje, limite)
        
        if limite and val >= limite:
            print(f"Error: El valor debe ser menor a {limite}.")
            return valor_positivo(mensaje, limite)
        
        return val
    except ValueError:
        print("Error: Ingrese un número válido.")
        return valor_positivo(mensaje, limite)

while Continuar.lower() == "s":
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Figuras 2D")
    print("2. Figuras 3D")
    print("3. TRIANGULO RECTANGULO")
    
    eleccion = input("Selecciona el número de tu opción: ")

    if not eleccion.isdigit() or int(eleccion) not in [1, 2, 3]:
        print("Opción no válida. Elige 1, 2 o 3.")
        continue

    if eleccion == "1":
        print("\n1. Triangulo\n2. Rectangulo\n3. Trapecio\n4. Circulo")
        figura_2D = input("Selecciona la figura: ")
        
        if figura_2D == "1":
            print("\n1. Area\n2. Base\n3. Altura\n4. Angulos")
            op = input("Operación: ")

            if op == "1":
                b, h = valor_positivo("Base (in): "), valor_positivo("Altura (in): ")
                print("El area es:", (b * h) / 2, "in²")

            elif op == "2":
                a, h = valor_positivo("Area (in²): "), valor_positivo("Altura (in): ")
                print("La base mide:", (2 * a) / h, "in")

            elif op == "3":
                a, b = valor_positivo("Area (in²): "), valor_positivo("Base (in): ")
                print("La altura es:", (2 * a) / b, "in")

            elif op == "4":
                a1 = valor_positivo("Angulo 1 (°): ", 180)
                a2 = valor_positivo("Angulo 2 (°): ", 180)

                if (a1 + a2) >= 180:
                    print("Error: La suma de los ángulos debe ser menor a 180°.")

                else:
                    print("El tercer angulo es:", 180 - (a1 + a2), "°")

        elif figura_2D == "2":
            print("\n1. Area\n2. Base\n3. Altura\n4. Perimetro")
            op = input("Operación: ")

            if op == "1":
                b, h = valor_positivo("Base (in): "), valor_positivo("Altura (in): ")
                print("El area es:", b * h, "in²")

            elif op == "2":
                a, h = valor_positivo("Area (in²): "), valor_positivo("Altura (in): ")
                print("La base mide:", a / h, "in")

            elif op == "3":
                a, b = valor_positivo("Area (in²): "), valor_positivo("Base (in): ")
                print("La altura mide:", a / b, "in")

            elif op == "4":
                b, h = valor_positivo("Base (in): "), valor_positivo("Altura (in): ")
                print("El perimetro es:", 2 * (b + h), "in")

        elif figura_2D == "3":
            print("\n1. Area\n2. Base mayor\n3. Base menor\n4. Altura")
            op = input("Operación: ")

            if op == "1":
                b1, b2, h = valor_positivo("B. Mayor (in): "), valor_positivo("B. Menor (in): "), valor_positivo("Altura (in): ")
                print("El area es:", ((b1 + b2) * h) / 2, "in²")

            elif op == "2":
                a, b2, h = valor_positivo("Area (in²): "), valor_positivo("B. Menor (in): "), valor_positivo("Altura (in): ")
                print("La base mayor mide:", ((2 * a) / h) - b2, "in")

            elif op == "3":
                a, b1, h = valor_positivo("Area (in²): "), valor_positivo("B. Mayor (in): "), valor_positivo("Altura (in): ")
                print("La base menor mide:", ((2 * a) / h) - b1, "in")

            elif op == "4":
                a, b1, b2 = valor_positivo("Area (in²): "), valor_positivo("B. Mayor (in): "), valor_positivo("B. Menor (in): ")
                print("La altura es:", (2 * a) / (b1 + b2), "in")

        elif figura_2D == "4":
            print("\n1. Area\n2. Radio\n3. Diametro")
            op = input("Operación: ")

            if op == "1":
                r = valor_positivo("Radio (in): ")
                print("El area es:", 3.1416 * (r ** 2), "in²")

            elif op == "2":
                a = valor_positivo("Area (in²): ")
                print("El radio mide:", (a / 3.1416) ** 0.5, "in")

            elif op == "3":
                r = valor_positivo("Radio (in): ")
                print("El diametro es:", 2 * r, "in")

    elif eleccion == "2":
        print("\n1. Paralelepipedo\n2. Cilindro\n3. Piramide\n4. Cono")
        figura_3D = input("Selecciona la figura: ")
        
        if figura_3D == "1":
            print("\n1. Volumen\n2. Area superficial\n3. Largo\n4. Ancho\n5. Altura")
            op = input("Operación: ")

            if op == "1":
                l, an, al = valor_positivo("Largo (in): "), valor_positivo("Ancho (in): "), valor_positivo("Altura (in): ")
                print("El volumen es:", l * an * al, "in³")

            elif op == "2":
                l, an, al = valor_positivo("Largo (in): "), valor_positivo("Ancho (in): "), valor_positivo("Altura (in): ")
                print("El area superficial es:", 2 * (l*an + l*al + an*al), "in²")

            elif op == "3":
                vol, an, al = valor_positivo("Volumen (in³): "), valor_positivo("Ancho (in): "), valor_positivo("Altura (in): ")
                print("El largo mide:", vol / (an * al), "in")

            elif op == "4":
                vol, l, al = valor_positivo("Volumen (in³): "), valor_positivo("Largo (in): "), valor_positivo("Altura (in): ")
                print("El ancho mide:", vol / (l * al), "in")

            elif op == "5":
                vol, l, an = valor_positivo("Volumen (in³): "), valor_positivo("Largo (in): "), valor_positivo("Ancho (in): ")
                print("La altura mide:", vol / (l * an), "in")


        elif figura_3D == "2":
            print("\n1. Volumen\n2. Area superficial\n3. Radio\n4. Altura")
            op = input("Operación: ")

            if op == "1":
                r, h = valor_positivo("Radio (in): "), valor_positivo("Altura (in): ")
                print("El volumen es:", 3.1416 * (r**2) * h, "in³")

            elif op == "2":
                r, h = valor_positivo("Radio (in): "), valor_positivo("Altura (in): ")
                print("El area superficial es:", 2 * 3.1416 * r * (r + h), "in²")

            elif op == "3":
                vol, h = valor_positivo("Volumen (in³): "), valor_positivo("Altura (in): ")
                print("El radio mide:", (vol / (3.1416 * h))**0.5, "in")

            elif op == "4":
                vol, r = valor_positivo("Volumen (in³): "), valor_positivo("Radio (in): ")
                print("La altura mide:", vol / (3.1416 * (r**2)), "in")


        elif figura_3D == "3":
            print("\n1. Volumen\n2. Area base\n3. Altura")
            op = input("Operación: ")

            if op == "1":
                ab, h = valor_positivo("Area base (in²): "), valor_positivo("Altura (in): ")
                print("El volumen es:", (ab * h) / 3, "in³")

            elif op == "2":
                vol, h = valor_positivo("Volumen (in³): "), valor_positivo("Altura (in): ")
                print("El area de la base es:", (3 * vol) / h, "in²")

            elif op == "3":
                vol, ab = valor_positivo("Volumen (in³): "), valor_positivo("Area base (in²): ")
                print("La altura es:", (3 * vol) / ab, "in")

        elif figura_3D == "4":
            print("\n1. Volumen\n2. Radio\n3. Altura")
            op = input("Operación: ")

            if op == "1":
                r, h = valor_positivo("Radio (in): "), valor_positivo("Altura (in): ")
                print("El volumen es:", (3.1416 * (r**2) * h) / 3, "in³")

            elif op == "2":
                vol, h = valor_positivo("Volumen (in³): "), valor_positivo("Altura (in): ")
                print("El radio mide:", ((3 * vol) / (3.1416 * h))**0.5, "in")

            elif op == "3":
                vol, r = valor_positivo("Volumen (in³): "), valor_positivo("Radio (in): ")
                print("La altura mide:", (3 * vol) / (3.1416 * (r**2)), "in")

    elif eleccion == "3":
        print("\n1. Hipotenusa\n2. Cateto faltante\n3. Area\n4. Perimetro")
        op = input("Operación: ")

        if op == "1":
            c1, c2 = valor_positivo("Cateto 1 (in): "), valor_positivo("Cateto 2 (in): ")
            print("Hipotenusa:", (c1**2 + c2**2)**0.5, "in")

        elif op == "2":
            hip, c1 = valor_positivo("Hipotenusa (in): "), valor_positivo("Cateto conocido (in): ")

            if hip <= c1: 
                print("Error: La hipotenusa debe ser mayor al cateto.")

            else: 
                print("Cateto faltante:", (hip**2 - c1**2)**0.5, "in")

        elif op == "3":
            b, h = valor_positivo("Base (in): "), valor_positivo("Altura (in): ")
            print("Area:", (b * h) / 2, "in²")

        elif op == "4":
            c1, c2 = valor_positivo("Cateto 1 (in): "), valor_positivo("Cateto 2 (in): ")
            hip = (c1**2 + c2**2)**0.5
            print("Perimetro:", c1 + c2 + hip, "in")

    Continuar = input("\n¿Deseas realizar otra operación? (s/n): ")

print("¡Gracias por usar la calculadora!")
