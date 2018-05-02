/** fichier SimpleFrameworkMain.java
Execution :
javac *.java
cd /home/evelyne/Documents/3TC/ELP/Java/reflection
java fr/insalyon/tc/framework/SimpleFrameworkMain Bee

Java est un langage réflexif : il donne la possibilité pour un programme en cours
d’exécution d’examiner son propre état et d’agir sur ce dernier.

La réflexivité de Java contribue à sa flexibilité et à l’usage répandu de frameworks,
mais elle a un coût à prendre en compte pour envisager son usage, car :
    l’appel aux méthodes réflexives (getMethod, newInstance, etc.) ont un surcoût,
    et le code exploitant la réflexivité est moins lisible et plus complexe à comprendre
    que lorsque les appels sont directs.

Bref, la réflexivité ne devrait être utilisé que lorsqu’aucune autre forme de programmation
n’est appropriée.
*/

package fr.insalyon.tc.framework;
import fr.insalyon.tc.framework.Animal;

//imagine this is the entry point for a framework, this can not be changed
public class SimpleFrameworkMain {

    public static void main(String[] args) {

	if (args.length < 1) {
	    System.err.println("You must provide the name of a class that extends Animal");
	} else {
	    String yourClassName = args[0];

	    try {

		Class<?> yourClass = Class.forName(yourClassName);
		Animal a = (Animal) yourClass.newInstance();
		System.out.println(yourClassName + " " + a.scream());

	    } catch (ClassNotFoundException e) {
		System.err.println("Class called '" + yourClassName + "' not found");
	    } catch (InstantiationException e) {
		System.err.println("Class called '" + yourClassName + "' cannot be instantiated");
	    } catch (IllegalAccessException e) {
		System.err.println("Class called '" + yourClassName + "' cannot be used");
	    }
	}
    }
}
