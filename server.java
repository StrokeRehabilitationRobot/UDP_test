import java.io.*;
import java.net.*;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.Arrays;


class UDPServer
{
    static DatagramSocket serverSocket;
    static int packetSize;
    static  int numFloats;
    static  ByteOrder be;
    static byte[] receiveData;
    static byte[] sendData;
    static  float[] msg;

    public static void main(String args[]) throws Exception
    {

        serverSocket = new DatagramSocket(9876);
        packetSize = 64;
        numFloats = (packetSize / 4) - 1;
        be = ByteOrder.LITTLE_ENDIAN;

        receiveData = new byte[packetSize];
        sendData = new byte[packetSize];

        ByteBuffer.wrap(sendData).order(be).putInt(0, 2).array();
        msg = new float[]{2,2,2,2,2,2,2,2};
        printArray(msg);
        sendData = command(37, msg);
        printArray(parse(sendData));

        while(true)
        {
            DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
            serverSocket.receive(receivePacket);
            //System.out.println(receivePacket.getData());
            printArray(receivePacket.getData());

            InetAddress IPAddress = receivePacket.getAddress();
            int port = receivePacket.getPort();
            //   sendData = msg.getBytes();
            DatagramPacket sendPacket =
            new DatagramPacket(sendData, sendData.length, IPAddress, port);
            serverSocket.send(sendPacket);
        }
    }

    static  byte[] command(int idOfCommand, float[] values)
    {
        byte[] message = new byte[packetSize];
        ByteBuffer.wrap(message).order(be).putInt(0, idOfCommand).array();
        for (int i = 0; i < numFloats && i < values.length; i++) {
            int baseIndex = (4 * i) + 4;
            ByteBuffer.wrap(message).order(be).putFloat(baseIndex, values[i]).array();
        }
        return message;
    }

    static float[] parse(byte[] bytes) {
        float[] returnValues = new float[numFloats];

        // println "Parsing packet"
        for (int i = 0; i < 1; i++) {
            int baseIndex = i ;
            returnValues[i] = ByteBuffer.wrap(bytes).order(be).getFloat(baseIndex);
        }

        return returnValues;
    }

    static void printArray(float[] anArray) {
        System.out.println(Arrays.toString(anArray));
    }

    static void printArray(byte[] anArray) {
        System.out.println(Arrays.toString(anArray));
    }
}
