import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;

public class Cipher {

	static ArrayList<ArrayList<Integer>> encrypt(State KEY , State PlainText) {
		// 128bit AES 
		// 10 rounds
		
		ArrayList<ArrayList<ArrayList<Integer>>> Keys = KeyExpansion.Expansion(KEY);
		
		State Key = new State(Keys.get(0));
		State newState = new State(Opperations.AddRoundKEY(Key, PlainText));
		//System.out.println(newState);
		
		for(int round = 1 ; round<=9;round++) {
			
			State SubedState = new State(Opperations.SubIntegers(newState));
			State ShiftedState = new State(ShiftRows.ShiftRow(SubedState));
			State MixedState =  new State(MixColumns.MixColumn(ShiftedState));
			Key.stateArray2D = Keys.get(round);
			newState.stateArray2D = Opperations.AddRoundKEY(Key , MixedState);
			//System.out.println(newState);
			
		}
		//System.out.println(newState);
		State SubedLastState = new State(Opperations.SubIntegers(newState));
		State ShiftedLastState = new State(ShiftRows.ShiftRow(SubedLastState));
		Key.stateArray2D = Keys.get(10);
		State EncryptedState = new State(Opperations.AddRoundKEY(Key , ShiftedLastState));
		
		return EncryptedState.stateArray2D;
		
		
		
		
		
		
		
		
		
	}
	static ArrayList<ArrayList<Integer>> decrypt(State KEY , State EncryptedText) {
		// 128bit AES 
		// 10 rounds
		
		ArrayList<ArrayList<ArrayList<Integer>>> Keys = KeyExpansion.Expansion(KEY);
		
		State Key = new State(Keys.get(10));
		//System.out.println();
		//System.out.println(10);
		//System.out.println(EncryptedText);
		State newStateAD = new State(Opperations.AddRoundKEY(Key , EncryptedText));
		State ShiftedState = new State(InvShiftRows.InvShiftRow(newStateAD));
		//System.out.println();
		State newState = new State(Opperations.InvSubIntegers(ShiftedState));
		//System.out.println(newState);
		
		
		for(int round = 1 ; round<=9;round++) {
			//System.out.println(round);
			//System.out.println(10-round);
			//System.out.println(newState);
			Key.stateArray2D = Keys.get(10-round);
			newState.stateArray2D = Opperations.AddRoundKEY(Key, newState);
			State MixedState =  new State(MixColumns.InvMixColumn(newState));
			State ShiftedStated= new State(InvShiftRows.InvShiftRow(MixedState));
			State SubedState = new State(Opperations.InvSubIntegers(ShiftedStated));
			newState.stateArray2D = SubedState.stateArray2D;
			
			
			
			
			
			
		}
		
		Key.stateArray2D = Keys.get(0);
		State DecryptedState = new State(Opperations.AddRoundKEY(Key , newState));
		//State ShiftedStated= new State(InvShiftRows.InvShiftRow(DecryptedStated));
		//State DecryptedState = new State(Opperations.InvSubIntegers(ShiftedStated));
		//displayHex(DecryptedState.stateArray2D);
		return DecryptedState.stateArray2D;
		
		
		
		
		
		
		
		
		
	}
	private static String hexToAscii(String hex) {
	    
	    
	    StringBuilder output = new StringBuilder();
	    for (int i = 0; i < hex.length(); i+=2) {
	        String str = hex.substring(i, i+2);
	        output.append((char)Integer.parseInt(str, 16));
	    }
	    //System.out.println(output);
	    return output.toString();
	}
	static String displayHex(ArrayList<ArrayList<Integer>> encryptedText) {
		String J = "";
		for(int i  = 0; i<4;i++) {
			
			for(int j  = 0; j<4;j++) {
				String s  = Integer.toHexString(encryptedText.get(j).get(i)).toUpperCase();
				
				if (s.length() ==2) {
					//System.out.print(Integer.toHexString(encryptedText.get(j).get(i)).toUpperCase());
					J+=Integer.toHexString(encryptedText.get(j).get(i)).toUpperCase();
				}
				
				if (s.length() !=2) {
					//System.out.print("0" + Integer.toHexString(encryptedText.get(j).get(i)).toUpperCase());
					J+="0" + Integer.toHexString(encryptedText.get(j).get(i)).toUpperCase();
				}
				
				
				
			}
			 
		}
		//System.out.println();
		//System.out.println( hexToAscii(J));
		return  hexToAscii(J);
			
		
	}
	
	static void Encrypt(State KEY , String TEXT) throws IOException {
		int j = 0;
		int k = 15;;
		fileReader Text = new fileReader(TEXT);
		//System.out.println(Text.text.length());
		//System.out.println( (int)Text.text.length()/16);
		String S = "";
		for(int i = 0 ; i< (int)Text.text.length()/16;i++) {
			
			String Temp = Text.text.substring(j,k+1);
			//System.out.println(Temp);
			
			
			
			j+=16;
			k+=16;
			State pText = new State(Temp);
			//System.out.println(pText);
			ArrayList<ArrayList<Integer>> encryptedText = encrypt(KEY,pText);
			//System.out.println(State.toString(encryptedText));
			S+= displayHex(encryptedText);
			
			
			
			
		}
		fileWrite encryptedFile = new fileWrite(S,TEXT);
		System.out.println("Text is ENCRYPTED");
	}
	static void Decrypt(State KEY , String TEXT) throws IOException {
		int j = 0;
		int k = 15;;
		fileReader Text = new fileReader(TEXT);
		//System.out.println(Text.text.length());
		//System.out.println( (int)Text.text.length()/16);
		String D ="";
		for(int i = 0 ; i< (int)Text.text.length()/16;i++) {
			
			String Temp = Text.text.substring(j,k+1);
			
			//System.out.println(Temp);
			j+=16;
			k+=16;
			State pText = new State(Temp);
			//System.out.println(pText);
			ArrayList<ArrayList<Integer>> decryptedText = decrypt(KEY,pText);
			//System.out.println(State.toString(encryptedText));
			D+=displayHex(decryptedText);
			
			
			
			
		}
		fileWrite decryptedFile = new fileWrite(D,TEXT);
		System.out.println("Text is DECRYPTED");
	}
	
	
	
	
}
