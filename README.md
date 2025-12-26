# picoCTF – Crack the Power (Medium)

This repository contains my write-up and Python solution for the picoCTF cryptography challenge **“Crack the Power” (Medium)**.

The challenge demonstrates how cryptographic systems can fail due to **implementation weaknesses**, even when the underlying algorithm (RSA) is mathematically secure.

---

## 🔑 Key Learnings
- RSA security heavily depends on correct parameter selection  
- Very small public exponents without proper padding can leak plaintext  
- Cryptographic failures often occur due to implementation mistakes, not algorithmic flaws  

---

## 🛠️ Approach
- Carefully analyzed RSA parameters instead of blindly relying on automated tools  
- Identified that modular reduction did not occur due to a small public exponent  
- Used a binary search technique to compute the integer *e-th root* of the ciphertext  
- Converted the recovered integer into readable bytes using Python  
- Solved the entire challenge using **Termux on a mobile device**

---

## 📂 Files
- `solve.py` — Python script implementing the solution logic  
- `README.md` — Challenge write-up and explanation  

---

## ⚠️ Ethical Note
The flag has **not been shared** in this repository to respect picoCTF rules and ethical CTF practices.

---

## 🌱 Takeaway
Strong cryptography is not just about using secure algorithms — it is about **correct design, proper parameters, and secure implementation**.

Building fundamentals step by step 🚀
