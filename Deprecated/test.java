import java.io.CharArrayReader;
import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;
import java.util.Arrays;
import java.io.IOException;

public class test {
	public class BinarytoDecimal {
		public int BinaryToDecimal(Long binaryNumber) {
			String value = Long.toString(binaryNumber);
			int output = 0;
			for (int position = 0; position < value.length(); position++) {
				if (value.charAt(position) == '1') {
					if (position == value.length() - 1) {
						output++;
					} else {
						output += Math.pow(2, value.length() - 1 - position);
					}
				} else if (value.charAt(position) == '0') {
	
				} else {
					System.err.println("Make sure you only input binary values");
				}
			}
			return output;
		}
	}
	public static void main(String[] args) {
		if (args[0].substring(args[0].length() - 3, args[0].length()).equals(".bs")) {
			String theString = "";
			try {
				File file = new File(args[0]);
				Scanner scanner = new Scanner(file);
				char temp = 'X';
				int counter = 0;
				String output = "";
				theString = scanner.nextLine();
				while (scanner.hasNextLine()) {
					theString += scanner.nextLine();
				}
				char[] charArray = theString.toCharArray();
				char[] chars = new char[charArray.length];
				for (int i = 0; i < charArray.length; i++) {
					if (charArray[i] == '0' || charArray[i] == '1') {
						temp = charArray[i];
						counter++;
						if (counter == 8) {
							System.out.println(chars);
							chars = Arrays.copyOf(chars, chars.length + 1);
							chars[chars.length - 1] = temp;
							temp = 'X';
							counter = 0;
						}
					}
				}
				for (int i = 0; i < chars.length; i++) {
					// output += chars[i];
					output += String.valueOf(Character.forDigit(chars[i], 2));
					// output += BinaryToDecimal(Integer.parseInt(String.valueOf(chars[i]))).toString();
				}
				System.out.println("output = \n" + output + "\n\nchars = " + chars + " chars len = " + chars.length);
			} catch (IOException e) {
				System.out.println("An error occurred.");
				e.printStackTrace();
			}
		}
	}
}