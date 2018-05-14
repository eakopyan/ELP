/** Flux (streams)
Un flux est une série d’informations envoyée sur un canal de communication entre deux entités. Il existe 3 flux standards :
* System.out -> entre l’application et l’écran pour transmettre une information
* System.err -> entre l’application et l’écran pour indiquer une erreur
* System.in -> entre le clavier et l’application
Autres flux : fichiers (java.io.File), socket réseau (java.net.socket)
*/

// Exemple System.in
import java.io.IOException;
public class MainClass {
  public static void main(String[] args) throws IOException {
    System.out.println("Entrez un caractère");
    int inChar = System.in.read();
    System.out.println("Vous avez saisi: "+inChar);
  }
}

// Exemple flux de fichiers
import java.io.File;
public class MainClass {
  public static void main(String[] args) {
    
    // instanciation des entités
    File f1 = new File(“/tmp/toto”);
    File f2 = new File(“/tmp/titi”);
    
    // instanciation des émetteurs/récepteurs
    FileInputStream fin = new FileInputStream(f1);
    FileOutputStream fout = new FileOutputStream(f2);
    
    // réception (lecture) ou émission (écriture)
    val = fin.read(); // read() renvoie un int représentant la valeur (0 à 255) de l'octet lu
    /** Variante à read() : int read(byte[] b)
    Lit un certain nombre d'octets et les copie dans le buffer b
    Renvoie le nombre d'octets lus
    */
    
    fout.write(val); // write(int val) écrit la valeur val dans le fichier
    /** Variante à write() : void write(byte[] b)
    Ecrit les octets du tableau d'octets b
    */
    
    fin.close();
    fout.close();
    
  }
}


// Exercice 1 : copie de fichiers

import java.io.IOException;
import java.io.File;

public class Copy {
  public static void main(String[] args) {
    FileInputStream fin;
    FileOutputStream fout;
    
    switch(args.length) {
      case 0 : // lecture et écriture sur la sortie standard
        fin = new FileInputStream(System.in);
        fout = new FileOutputStream(System.out);
        copy(fin, fout);
        break;
        
      case 1 : // lecture fichier src et écriture sur sortie standard
        fin = new FileInputStream(args[0]);

        fout = new FileOutputStream(System.out);
        copy(fin, fout);
        break;
        
      case 2 : // lecture fichier src et écriture fichier dest        
        fin = new FileInputStream(args[0]);
        fout = new FileOutputStream(args[1]);
        copy(fin, fout);
        break;
        
      default :
        System.err.println("Veuillez entrer au maximum 2 arguments.");
        break;
    }
  }
  
  private static void copy(InputStream is, OutputStream os) throws IOException {
    int val = fin.read();
    fout.write(val);
  }
   
}
/** Décoration de flux
Un décorateur réalise des traitements supplémentaires avant ou après la transmission qui est déléguée au 
flux à partir duquel il est construit.
*/

// Exemple flux de données
FileInputStream fis = new FileInputStream("source");
DataInputStream dis = new DataInputStream(fis);
double d = dis.readDouble();
  
FileOutputStream fos = new FileOutputStream("cible");
DataOutputStream dos = new DataOutputStream(fos);
dos.writeDouble(123.456);
  
  
// Exemple flux de caractères
FileInputStream fis = new FileInputStream("source.txt");
InputStreamReader r = new InputStreamReader(fis);
//equivalent: FileReader r = new FileReader("source.txt");
char c = (char) r.read();
  
FileOutputStream fos = new FileOutputStream("cible.txt");
OutputStreamWriter w = new OutputStreamWriter(fos);
//equivalent: FileWriter w = new FileWriter("cible.txt");
w.write( (int) 'a' );
  
  
// Exemple flux de lignes
FileInputStream fis = new FileInputStream("source.txt");
BufferedReader in = new BufferedReader( new InputStreamReader(fis) );
String line = in.readLine();
  
FileOutputStream fos = new FileOutputStream("cible.txt");
PrintWriter out = new PrintWriter( new OutputStreamWriter(fos) );
out.println("blabla");
  
  
/** Flux d'objets : sérialisation
La sérialisation (= serialization) est le processus de transformation d’un objet en flux (série) d’octets. 
La déserialisation est le processus inverse.
Un objet peut ainsi être facilement sauvegardé dans un fichier ou transféré sur le réseau.
*/
import java.io.Serializable;
  // voir fichiers Message.java et EcrireMessage.java
  
  
// ==================================================================================================
/** Sockets réseau
Le package java.net fournit un ensemble de classes pour l’implémentation d’applications réseau comme les adresses, modélisant des 
adresses IP, ou les sockets, modélisant les extrémités d’un canal de communication bidirectionnelle entre deux processus via le 
réseau.
*/
import java.net.* ;

// La classe SocketServer permet au processus serveur d’attendre et d’accepter la connexion d’un processus client.
ServerSocket connection = new ServerSocket(numeroPort);
Socket socket = connection.accept(); // renvoie un objet Socket lorsque la connexion est établie

Socket socket = new Socket("localhost", numeroPort); // côté client

InputStream is = socket.getInputStream();
OutputStream os = socket.getOutputStream();
