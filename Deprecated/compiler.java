import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;
import java.util.Arrays;
import java.io.IOException;

public class compiler {
	public static void main(String[] args) {
		// System.out.println("\'"+args[0].substring(args[0].length()-3, args[0].length())+"\'");
		if (args[0].substring(args[0].length()-3, args[0].length()).equals(".bs")) {
			File f = new File(args[0]);
			// Scanner f_reader = new Scanner(f);
			char temp = Character.MIN_VALUE;
			int counter = 0;
			Long tempVal = f.length();
			char[] chars = new char[tempVal.intValue()];
			String output = "";
			for (int i = 0; i < f.length(); i++) {
				if (f.charAt(i) == '0' || f.charAt(i) == '1') {
					temp += (char)i;
					counter++;
					if (counter == 8) {
						chars = Arrays.copyOf(chars, chars.length + 1);
						chars[chars.length - 1] = temp;
						temp = Character.MIN_VALUE;
						counter = 0;
					}
				}
			}
			for (int i = 0; i < chars.length; i++) {
				System.out.println(chars);
				System.exit(1);
				// output += String.valueOf(Character.forDigit(chars.charAt(i), 2));
				// System.out.println(output);
			}
			try {
				File g = new File(args[0].substring(0, args[0].length()-3)+".py");
				// FileWriter h = new FileWriter(args[0].substring(args[0].length(), args[0].length()-3)+".py");
				FileWriter h = new FileWriter(g);
				h.write(output);
				System.out.println("Created: "+args[0].substring(0, args[0].length()-3)+".py");
				h.close();
			} catch (IOException e) {
				System.out.println("An error occurred.");
				e.printStackTrace();
			}
		} else {
			System.err.println("This isn't bs!");
			System.exit(1);
		}
	}
}