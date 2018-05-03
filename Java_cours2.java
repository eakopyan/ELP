/** Conteneurs : https://perso.liris.cnrs.fr/tristan.roussillon/ens/java/2018/html/TD5Conteneurs.html
Collection : type de base, ensemble d'objets
List : collection d'objets ordonnée (implémentation de Collection). L'ordre de parcours de la liste est garanti.
Set : liste d'objets sans doublon (implémentation de Collection)
Map : conteneur de paires clé-valeur 

ArrayList : liste modélisée en mémoire par un tableau dynamique (allocations, etc)
LinkedList : simple liste chaînée. Les objets ne sont pas interconnectés en mémoire

HashMap : tableau de hashs, il n'y a pas d'ordre garanti
TreeMap : arbre binaire de recherche */

// ====================================== fichier Etudiant.java =============================================
/**
 * Classe modelisant un etudiant caracterise
 * par son numero (unique), son prenom et son nom
 */
public class Etudiant {

    ///identifiant unique de l'etudiant
    private Integer numero; 
    ///prenom
    private String prenom; 
    ///nom de famille
    private String nom; 

    /**
     * Constructeur
     * @param numero
     * @param prenom
     * @param nom 
     */
    public Etudiant(Integer numero, String prenom, String nom) {
	this.numero = numero; 
	this.prenom = prenom; 
	this.nom = nom; 
    }

    /**
     * Indique si le nom de l'etudiant et un nom donné sont identiques
     * @param unNom un nom donne
     * @return 'True' si les deux noms sont les memes, 'False' sinon
     */
    public boolean aCeNom(String unNom) {
	return (nom.equals(unNom)); 
    }

    /**
     * @return une representation textuelle de l'etudiant 
    */ 
    @Override
    public String toString() {
	return super.toString() + "[" + nom + " " + prenom + ", n° " + numero + "]"; 
    }
}


//========================================== fichier GroupeEtudiant.java =================================================
import java.util.*;

public class GroupeEtudiant {
  
  private ArrayList groupe;
  
  public GroupeEtudiant(){
    this.groupe = new ArrayList();
  }
  
  void ajout(Etudiant e){
    boolean isAdded = this.add(e);
  }
}

//=========================================== fichier ClientEtudiant.java ================================================

import java.util.*;

public class ClientEtudiant {
  public static void main(String[] args) {

    GroupeEtudiant TC2 = new GroupeEtudiant();
    Etudiant toto = new Etudiant(123456, "Toto", NULL);
    Etudiant lulu = new Etudiant(789101, "Lulu", "Hono");

    TC2.ajout(toto);
    TC2.ajout(lulu);

  }
} 
  
  
  
  
  
  
  
  
