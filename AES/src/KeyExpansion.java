import java.util.ArrayList;

public class KeyExpansion {

	
	static ArrayList<ArrayList<ArrayList<Integer>>> Expansion(State key) {
		   
		ArrayList<ArrayList<Integer>> keyArray = Opperations.copyArray(key);
		ArrayList<ArrayList<Integer>> words = new  ArrayList<ArrayList<Integer>>();
		int counter = 7;
		int wordCounter = 4;
		int roundCounter = 1;
		
		for(int i = 0; i< keyArray.size(); ++i) {
			ArrayList<Integer> word = Opperations.extractColumn(i, keyArray);
			words.add(word);
			
		}
		//System.out.println(words);
		ArrayList<Integer> vector = transformVector(words.get(3),0);
		
		while(wordCounter <= 40) {
			ArrayList<Integer> word1 = XorVector(words.get(wordCounter -4)  , vector );
			ArrayList<Integer> word2 = XorVector(words.get(wordCounter -3) , word1 );
			ArrayList<Integer> word3 = XorVector(words.get(wordCounter -2) , word2 );
			ArrayList<Integer> word4 = XorVector(words.get(wordCounter -1) , word3 );
			words.add(word1);
			words.add(word2);
			words.add(word3);
			words.add(word4);
			
			
			
			if(roundCounter != 10) {
				vector = transformVector(words.get(counter),roundCounter);
				
			}
			
			roundCounter+=1;
			
			counter +=4;

			wordCounter+=4;
			
			
			
		}
		
		
		return FormatMatrixKeys(words);
		
	}
	
	static ArrayList<Integer> transformVector(ArrayList<Integer> vector , int round) {

		return XorRoundConst(round , SubWord(RotWord(vector)) );
	
	}
	
	static ArrayList<Integer> SubWord(ArrayList<Integer> Vector){
		
		ArrayList<Integer> vector = copyVector(Vector);
		
		for(int j = 0 ; j<vector.size();++j) {
			SubByte letter = new SubByte(vector.get(j));
			
			vector.set(j ,letter.SubedByte );
		}
		
		
		
		
		return vector;
	}
	
	
	static ArrayList<Integer> RotWord(ArrayList<Integer> Vector) {
		ArrayList<Integer> vector = copyVector(Vector);
		
		
		int temp = vector.get(3);
		for(int j = vector.size()-1 ; j>=1;--j) {
			int temp2 = vector.get(j-1);
			vector.set(j-1, temp);
			temp = temp2;
		}
		vector.set(3, temp);
		/*
		for(int i = 0 ; i<4 ; ++i) {
			System.out.println(Integer.toHexString(vector.get(i)));
		}
		System.out.println();
		System.out.println();*/
		return vector;
		
		
		
		
		
	}
	
	
	static ArrayList<Integer> getRoundConsts(){
		ArrayList<Integer> rcons = new ArrayList<Integer>();
		int rcon =1;
		
		
		for(int round  = 1 ; round <10;round++ ) {
			rcons.add(rcon);
			rcon = (rcon <<1 )^(0x11b & -(rcon>>7));
			//System.out.println(Integer.toHexString(rcon));
			
		}
		rcons.add(rcon);
		//System.out.println(rcons);
		return rcons;
		
		
	}
	static ArrayList<Integer> copyVector(ArrayList<Integer> word){
		ArrayList<Integer> vector = new ArrayList<Integer>();
		for(int i = 0; i<word.size();++i) {
			vector.add(word.get(i));
		}
		
		
		
		return vector;
		
	}
	
	
	static ArrayList<Integer> XorRoundConst(int round , ArrayList<Integer> word ) {
		ArrayList<Integer> rcons = getRoundConsts();
		ArrayList<Integer> vector = copyVector(word);
		int value = rcons.get(round) ^ vector.get(0);
		vector.set(0,value);
		return vector;
	}
	
	static ArrayList<Integer> XorVector( ArrayList<Integer> word , ArrayList<Integer> vector){
		 ArrayList<Integer> newWord = new  ArrayList<Integer>();
		 
		 for(int i = 0;i<word.size();++i) {
			 int value = word.get(i) ^ vector.get(i);
			 newWord.add(value);
		 }
		 return newWord;
		 
	}
	
	static ArrayList<ArrayList<Integer>> createBlock( ArrayList<Integer> c1 ,  ArrayList<Integer> c2 ,  ArrayList<Integer> c3 ,  ArrayList<Integer> c4){
		
		ArrayList<ArrayList<Integer>> array2D = new ArrayList<ArrayList<Integer>>() ; 
		ArrayList<Integer> rowArray2D_1 = new ArrayList<Integer>();
		ArrayList<Integer> rowArray2D_2 = new ArrayList<Integer>();
		ArrayList<Integer> rowArray2D_3 = new ArrayList<Integer>();
		ArrayList<Integer> rowArray2D_4 = new ArrayList<Integer>();
		
		for(int i = 0 ; i<4;++i) {
			if(i == 0) {
				
				rowArray2D_1.add(c1.get(0));
				rowArray2D_1.add(c2.get(0));
				rowArray2D_1.add(c3.get(0));
				rowArray2D_1.add(c4.get(0));
			}else if(i == 1) {
				rowArray2D_2.add(c1.get(1));
				rowArray2D_2.add(c2.get(1));
				rowArray2D_2.add(c3.get(1));
				rowArray2D_2.add(c4.get(1));
			}else if(i == 2) {
				rowArray2D_3.add(c1.get(2));
				rowArray2D_3.add(c2.get(2));
				rowArray2D_3.add(c3.get(2));
				rowArray2D_3.add(c4.get(2));
			}else if(i == 3) {
				rowArray2D_4.add(c1.get(3));
				rowArray2D_4.add(c2.get(3));
				rowArray2D_4.add(c3.get(3));
				rowArray2D_4.add(c4.get(3));
			}
			
		}
		array2D.add(rowArray2D_1);
		array2D.add(rowArray2D_2);
		array2D.add(rowArray2D_3);
		array2D.add(rowArray2D_4);
		
		
		return array2D;
		
		
	}
	
	static ArrayList<ArrayList<ArrayList<Integer>>> FormatMatrixKeys(ArrayList<ArrayList<Integer>> words){
		
		ArrayList<ArrayList<ArrayList<Integer>>> KeyList = new ArrayList<ArrayList<ArrayList<Integer>>>();
		for(int i = 0; i<44;) {
			ArrayList<ArrayList<Integer>> block = createBlock(words.get(i),words.get(i+1),words.get(i+2),words.get(i+3));
			i+=4;
			KeyList.add(block);
		}
		return KeyList;
		
	}
	
	
	
	
	
	
	
	
}
