import java.util.ArrayList;

public class SHA256 {
	String hex ="";
	
	SHA256(String msg){
		Word word = new Word(msg);
		Hash hash= new Hash(word);
		convToHex(hash.digest);
		
		
		
	}
	
	void convToHex(ArrayList<ArrayList<Long>> digest){
		for(ArrayList<Long> i : digest) {
			long temp = SigmaFunctions.convBitArray(i);
			this.hex += Long.toHexString(temp);
		}
	}
}
