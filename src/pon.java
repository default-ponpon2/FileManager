class Student{
    
    private int id;
    private String name;
    
    public Student(int id, String name){
        this.id = id;
        this.name = name;
    }
    
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    
    //for printing purpose
    public String toString(){
        return "(" + getId() + " => " + getName() + ")";
    }
 
}
 
//this comparator will sort Student objects in ascending order by id
class StudentComparator implements Comparator<Student>{
 
    public int compare(Student s1, Student s2) {
        return s1.getId() - s2.getId();
    }    
}
 
//this comparator will sort Student objects in descending order by id
class StudentDescendingComparator implements Comparator<Student>{
 
    public int compare(Student s1, Student s2) {
        return s2.getId() - s1.getId();
    }    
}
 
public class Example {
    public static void main(String[] args) {
        
        Student[] studentArray = { new Student(3, "Jack"), new Student(1, "Ryan"), new Student(2, "Adam") };
        System.out.println("object array before sorting: ");
        System.out.println( Arrays.toString(studentArray) ); 
        
        /*
         * To sort an object array by custom comparator, use
         * the sort method and specify the comparator object
         */
        //sort Student objects in the ascending order using the StudentComparator
        Arrays.sort(studentArray, new StudentComparator());
        
        System.out.println("object array after sorting in ascending order by id: ");
        System.out.println( Arrays.toString(studentArray) ); 
        
        /*
         * Similarly, sort an array of objects in descending order
         * using the sort method
         */
        //this will sort Student objects in the descending order using the StudentDescendingComparator
        Arrays.sort(studentArray, new StudentDescendingComparator());
 
        System.out.println("object array after sorting in descending order by id: ");
        System.out.println( Arrays.toString(studentArray) ); 
    }
}