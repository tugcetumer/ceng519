import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv("/content/sample_data/results.csv")

compileTimes = []
keyGenerationTimes = []
encryptionTimes = []
executionTimes = []
decryptionTimes = []
refExecutionTimes = []
mseTimes = []
node_counts = []

compileTime_avg = 0
keyGenerationTime_avg = 0
encryptionTime_avg = 0
executionTime_avg = 0
decryptionTime_avg = 0
referenceExecutionTime_avg = 0
mse_avg = 0

for i in range(1200):
  compileTime_avg+= data.CompileTime[i]
  keyGenerationTime_avg+= data.KeyGenerationTime[i]
  encryptionTime_avg+= data.EncryptionTime[i]
  executionTime_avg+= data.ExecutionTime[i]
  decryptionTime_avg+= data.DecryptionTime[i]
  referenceExecutionTime_avg+= data.ReferenceExecutionTime[i]
  mse_avg+= data.Mse[i]
  
  if i%100 == 99:
    compileTime_avg /= 100
    compileTimes.append(compileTime_avg)

    keyGenerationTime_avg /= 100
    keyGenerationTimes.append(keyGenerationTime_avg)

    encryptionTime_avg /= 100
    encryptionTimes.append(encryptionTime_avg)

    executionTime_avg /= 100
    executionTimes.append(executionTime_avg)

    decryptionTime_avg /= 100
    decryptionTimes.append(decryptionTime_avg)

    referenceExecutionTime_avg /= 100
    refExecutionTimes.append(referenceExecutionTime_avg)

    mse_avg /= 100
    mseTimes.append(mse_avg)

    node_counts.append(data.NodeCount[i])
    compileTime_avg = 0
    keyGenerationTime_avg = 0
    encryptionTime_avg = 0
    executionTime_avg = 0
    decryptionTime_avg = 0
    referenceExecutionTime_avg = 0
    mse_avg = 0

fig, axComp = plt.subplots()
axComp.stem(node_counts, compileTimes)
axComp.set(ylim=(2, 32))
axComp.set_title('Node Count vs Compile Time')
axComp.set_ylabel('Average Compile Time (ms)')
axComp.set_xlabel('Node Count')
axComp.set_xticks(node_counts)

for i, j in zip(node_counts, compileTimes):
   plt.text(i-1, j+0.2, '{:.2f}'.format(j))

plt.savefig("/content/asd/compTime.png")
plt.show()

fig, axKeyGen = plt.subplots()
axKeyGen.stem(node_counts, keyGenerationTimes)
axKeyGen.set(ylim=(48, 51))
axKeyGen.set_title('Node Count vs Key Generation Time')
axKeyGen.set_ylabel('Average Key Generation Time (ms)')
axKeyGen.set_xlabel('Node Count')
axKeyGen.set_xticks(node_counts)

for i, j in zip(node_counts, keyGenerationTimes):
   plt.text(i-1, j+0.2, '{:.2f}'.format(j))

plt.savefig("/content/asd/keyGenTime.png")
plt.show()

fig, axEnc = plt.subplots()
axEnc.stem(node_counts, encryptionTimes)
axEnc.set(ylim=(32, 34))
axEnc.set_title('Node Count vs Encyrption Time')
axEnc.set_ylabel('Average Encyrption Time (ms)')
axEnc.set_xlabel('Node Count')
axEnc.set_xticks(node_counts)

for i, j in zip(node_counts, encryptionTimes):
   plt.text(i-1, j+0.2, '{:.2f}'.format(j))

plt.savefig("/content/asd/encTime.png")
plt.show()

fig, axExe = plt.subplots()
axExe.stem(node_counts, executionTimes)
axExe.set(ylim=(200, 1100))
axExe.set_title('Node Count vs Execution Time')
axExe.set_ylabel('Average Execution Time (ms)')
axExe.set_xlabel('Node Count')
axExe.set_xticks(node_counts)

for i, j in zip(node_counts, executionTimes):
   plt.text(i-1, j+0.2, '{:.2f}'.format(j))

plt.savefig("/content/asd/exeTime.png")
plt.show()

fig, axDec = plt.subplots()
axDec.stem(node_counts, decryptionTimes)
axDec.set(ylim=(14, 15.5))
axDec.set_title('Node Count vs Decryption Time')
axDec.set_ylabel('Average Decryption Time (ms)')
axDec.set_xlabel('Node Count')
axDec.set_xticks(node_counts)

for i, j in zip(node_counts, decryptionTimes):
   plt.text(i-1, j+0.2, '{:.2f}'.format(j))

plt.savefig('/content/asd/decTime.png')
plt.show()

fig, axExe = plt.subplots()
axExe.stem(node_counts, mseTimes)
axExe.set(ylim=(0, 0.0001))
axExe.set_title('Node Count vs Mse')
axExe.set_ylabel('Average Mse')
axExe.set_xlabel('Node Count')
axExe.set_xticks(node_counts)

for i, j in zip(node_counts, mseTimes):
   plt.text(i-1, j+0.0001, '{:.5f}'.format(j))

plt.show()
