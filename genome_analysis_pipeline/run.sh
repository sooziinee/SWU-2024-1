#!/bin/bash

sample=$1
fq1=${sample}_1.fastq.gz
fq2=${sample}_2.fastq.gz

echo "##START: `date`" > ${sample}.log.txt

# PROGRAMS
BWA="/usr/bin/bwa"
SAMTOOLS="/usr/bin/samtools"
JAVA="/usr/bin/java"
PICARD="/home/ubuntu/etc/picard/picard.jar"
GATK="/home/ubuntu/etc/gatk/gatk-4.5.0.0/gatk-package-4.5.0.0-local.jar"
SNPEFF="/home/ubuntu/Downloads/snpEff/snpEff.jar"

# RESOURCES
REFERENCE="/home/ubuntu/etc/reference/chr21.fa.gz"

# FILES
mapped_sam="${sample}.chr21.sam"

