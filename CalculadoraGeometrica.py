print("Bienvenido a la calculadora Geometrica")
Continuar = "s"

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
        
        if not figura_2D.isdigit() or int(figura_2D) not in [1, 2, 3, 4]:
            print("Figura no válida.")
            continue

        try:
            if figura_2D == "1":
                print("\n1. Area\n2. Base\n3. Altura\n4. Angulos")
                op = input("Operación: ")

                if not op.isdigit() or int(op) not in range(1, 5): print("Opción no válida."); continue

                if op == "1":
                    b, h = float(input("Base: ")), float(input("Altura: "))
                    print("El area es:", (b * h) / 2)

                elif op == "2":
                    a, h = float(input("Area: ")), float(input("Altura: "))
                    print("La base mide:", (2 * a) / h)

                elif op == "3":
                    a, b = float(input("Area: ")), float(input("Base: "))
                    print("La altura es:", (2 * a) / b)

                elif op == "4":
                    a1, a2 = float(input("Angulo 1: ")), float(input("Angulo 2: "))
                    print("El tercer angulo es:", 180 - (a1 + a2))

            elif figura_2D == "2":
                print("\n1. Area\n2. Base\n3. Altura\n4. Perimetro")
                op = input("Operación: ")

                if not op.isdigit() or int(op) not in range(1, 5): print("Opción no válida."); continue

                if op == "1":
                    b, h = float(input("Base: ")), float(input("Altura: "))
                    print("El area es:", b * h)

                elif op == "2":
                    a, h = float(input("Area: ")), float(input("Altura: "))
                    print("La base mide:", a / h)

                elif op == "3":
                    a, b = float(input("Area: ")), float(input("Base: "))
                    print("La altura es:", a / b)

                elif op == "4":
                    b, h = float(input("Base: ")), float(input("Altura: "))
                    print("El perimetro es:", 2 * (b + h))

            elif figura_2D == "3":
                print("\n1. Area\n2. Base mayor\n3. Base menor\n4. Altura")
                op = input("Operación: ")

                if not op.isdigit() or int(op) not in range(1, 5): print("Opción no válida."); continue
                
                if op == "1":
                    b1, b2, h = float(input("B. Mayor: ")), float(input("B. Menor: ")), float(input("Altura: "))
                    print("El area es:", ((b1 + b2) * h) / 2)

                elif op == "2":
                    a, b2, h = float(input("Area: ")), float(input("B. Menor: ")), float(input("Altura: "))
                    print("La base mayor mide:", ((2 * a) / h) - b2)

                elif op == "3":
                    a, b1, h = float(input("Area: ")), float(input("B. Mayor: ")), float(input("Altura: "))
                    print("La base menor mide:", ((2 * a) / h) - b1)

                elif op == "4":
                    a, b1, b2 = float(input("Area: ")), float(input("B. Mayor: ")), float(input("B. Menor: "))
                    print("La altura es:", (2 * a) / (b1 + b2))

            elif figura_2D == "4":
                print("\n1. Area\n2. Radio\n3. Diametro")
                op = input("Operación: ")

                if not op.isdigit() or int(op) not in range(1, 4): print("Opción no válida."); continue

                if op == "1":
                    r = float(input("Radio: "))
                    print("El area es:", 3.1416 * (r ** 2))

                elif op == "2":
                    a = float(input("Area: "))
                    print("El radio mide:", (a / 3.1416) ** 0.5)

                elif op == "3":
                    r = float(input("Radio: "))
                    print("El diametro es:", 2 * r)

        except ValueError: print("Error: Ingresa solo números en las medidas."); continue
        except ZeroDivisionError: print("Error: No se puede dividir por cero."); continue


    elif eleccion == "2":
        print("\n1. Paralelepipedo\n2. Cilindro\n3. Piramide\n4. Cono")
        figura_3D = input("Selecciona la figura: ")

        if not figura_3D.isdigit() or int(figura_3D) not in [1, 2, 3, 4]:
            print("Figura no válida.")
            continue

        try:
            if figura_3D == "1":
                print("\n1. Volumen\n2. Area superficial\n3. Largo\n4. Ancho\n5. Altura")
                op = input("Que operacion deseas realizar?: ")
                
                if not op.isdigit() or int(op) not in range(1, 6): print("Opción no válida."); continue
                
                if op == "1":
                    l, an, al = float(input("Largo: ")), float(input("Ancho: ")), float(input("Altura: "))
                    print("El volumen es:", l * an * al)

                elif op == "2":
                    l, an, al = float(input("Largo: ")), float(input("Ancho: ")), float(input("Altura: "))
                    print("El area superficial es:", 2 * (l*an + l*al + an*al))

                elif op == "3":
                    v, an, al = float(input("Volumen: ")), float(input("Ancho: ")), float(input("Altura: "))
                    print("El largo mide:", v / (an * al))

                elif op == "4":
                    v, l, al = float(input("Volumen: ")), float(input("Largo: ")), float(input("Altura: "))
                    print("El ancho mide:", v / (l * al))

                elif op == "5":
                    v, l, an = float(input("Volumen: ")), float(input("Largo: ")), float(input("Ancho: "))
                    print("La altura mide:", v / (l * an))


            elif figura_3D == "2":
                print("\n1. Volumen\n2. Area superficial\n3. Radio\n4. Altura")
                op = input("Que operacion deseas realizar?: ")
                if not op.isdigit() or int(op) not in range(1, 5): print("Opción no válida."); continue
                
                if op == "1":
                    r, h = float(input("Radio: ")), float(input("Altura: "))
                    print("El volumen es:", 3.1416 * (r**2) * h)

                elif op == "2":
                    r, h = float(input("Radio: ")), float(input("Altura: "))
                    print("El area superficial es:", 2 * 3.1416 * r * (r + h))

                elif op == "3":
                    v, h = float(input("Volumen: ")), float(input("Altura: "))
                    print("El radio mide:", (v / (3.1416 * h))**0.5)

                elif op == "4":
                    v, r = float(input("Volumen: ")), float(input("Radio: "))
                    print("La altura mide:", v / (3.1416 * (r**2)))


            elif figura_3D == "3":
                print("\n1. Volumen\n2. Area de la base\n3. Altura")
                op = input("Que operacion deseas realizar?: ")

                if not op.isdigit() or int(op) not in range(1, 4): print("Opción no válida."); continue
                
                if op == "1":
                    ab, h = float(input("Area de la base: ")), float(input("Altura: "))
                    print("El volumen es:", (ab * h) / 3)

                elif op == "2":
                    v, h = float(input("Volumen: ")), float(input("Altura: "))
                    print("El area de la base es:", (3 * v) / h)

                elif op == "3":
                    v, ab = float(input("Volumen: ")), float(input("Area de la base: "))
                    print("La altura es:", (3 * v) / ab)

            elif figura_3D == "4":
                print("\n1. Volumen\n2. Radio\n3. Altura")
                op = input("Que operacion deseas realizar?: ")

                if not op.isdigit() or int(op) not in range(1, 4): print("Opción no válida."); continue
                
                if op == "1":
                    r, h = float(input("Radio: ")), float(input("Altura: "))
                    print("El volumen es:", (3.1416 * (r**2) * h) / 3)

                elif op == "2":
                    v, h = float(input("Volumen: ")), float(input("Altura: "))
                    print("El radio mide:", ( (3 * v) / (3.1416 * h) )**0.5)

                elif op == "3":
                    v, r = float(input("Volumen: ")), float(input("Radio: "))
                    print("La altura mide:", (3 * v) / (3.1416 * (r**2)))


        except (ValueError, ZeroDivisionError): print("Error en datos numéricos."); continue


    elif eleccion == "3":

        print("\n1. Hipotenusa\n2. Cateto faltante\n3. Area\n4. Perimetro")
        op = input("Operación: ")

        if not op.isdigit() or int(op) not in range(1, 5):
            print("Opción no válida.")
            continue

        try:
            if op == "1":
                c1, c2 = float(input("Cateto 1: ")), float(input("Cateto 2: "))
                print("Hipotenusa:", (c1**2 + c2**2)**0.5)

            elif op == "2":
                hip, c1 = float(input("Hipotenusa: ")), float(input("Cateto conocido: "))
                print("Cateto faltante:", (hip**2 - c1**2)**0.5)

            elif op == "3":
                b, h = float(input("Base: ")), float(input("Altura: "))
                print("Area:", (b * h) / 2)

            elif op == "4":
                c1, c2 = float(input("Cateto 1: ")), float(input("Cateto 2: "))
                hip = (c1**2 + c2**2)**0.5
                print("Perimetro:", c1 + c2 + hip)

        except ValueError: print("Error: Datos inválidos."); continue

    Continuar = input("\n¿Deseas realizar otra operación? (s/n): ")

print("¡Gracias por usar la calculadora!")
