import java.util.ArrayList;

public class ShiftRows {
    static ArrayList<Integer> duplicateArray(ArrayList<Integer> a1) {
        ArrayList<Integer> a2 = new ArrayList<Integer>();
        for(int i = 0 ; i<a1.size();i++) {
            a2.add(a1.get(i));
        }
        return a2;


    }
    static ArrayList<ArrayList<Integer>> ShiftRow(State word) {

        ArrayList<ArrayList<Integer>> array = Opperations.copyArray(word);
        ArrayList<ArrayList<Integer>> arrayDuplicate = Opperations.copyArray(word);

        for(int i = 1 ; i<array.size() ; ++i) {

            for(int j =array.get(i).size()-1;j>=0;--j) {

                try {
                    array.get(i).set(j-i,arrayDuplicate.get(i).get(j));
                }catch(IndexOutOfBoundsException  e) {
                    int J = array.get(i).size() - Math.abs(j-i);
                    array.get(i).set(J,arrayDuplicate.get(i).get(j));
                }


            }

        }

        return array;


    }
}
