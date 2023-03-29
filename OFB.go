package LM2_ECB_OFB

// Import relevant libraries
import (
	"crypto/aes"
	"crypto/cipher"
	"fmt"
)

// Main function with key and plaintext
func main() {
	key := []byte("0123456789abcdef")
	plaintext := []byte("exampleplaintext")

	block, err := aes.NewCipher(key)
	if err != nil {
		panic(err)
	}
	ciphertext := make([]byte, len(plaintext))

	// OFB encryption
	ofb := cipher.NewOFB(block, key[:aes.BlockSize])
	ofb.XORKeyStream(ciphertext, plaintext)

	fmt.Printf("OFB encrypted: %x\n", ciphertext)
}
