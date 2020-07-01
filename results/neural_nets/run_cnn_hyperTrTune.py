import os.path as osp
import subprocess
#from cnn_hyperTrTune import hyper


dna_datasets = [
    'CTCF', 'EP300', 'JUND', 'RAD21', 'SIN3A',
    'Pbde', 'EP300_47848', 'KAT2B', 'TP53', 'ZZZ3',
]

prot_datasets = [
    '1.1', '1.34', '2.19', '2.31', '2.34',
    '2.41', '2.8', '3.19', '3.25', '3.33',
]

nlp_datasets = [
    'AIMed', 'BioInfer', 'CC1-LLL', 'CC2-IEPA', 
    'CC3-HPRD50', 'DrugBank', 'MedLine'
]

datasets = prot_datasets + dna_datasets + nlp_datasets

for dataset in datasets:
    train_file = osp.join('../../data/', dataset + '.train.fasta')
    print("train_file = ", train_file)
    test_file = osp.join('../../data/', dataset + '.test.fasta')
    print("test_file = ", test_file)
    for trn_size in [1., 0.8, 0.6, 0.4, 0.2]:
    	for opt in ['sgd', 'adam']:
            for lr in [1e-2, 8e-3]: 
                #hyper(opt, lr, trn_size, train_file, test_file, dataset)

                command = ['python', 'cnn_hyperTrTune.py', '--trn', train_file,
                '--tst', test_file, '--trn_size', trn_size, '--lr', lr
                '--datasetTag', dataset, '--opt_mtd', opt, '--epochs', 20]
                print(' '.join(command))
                output = subprocess.check_output(command)
