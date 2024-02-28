import subprocess
import os

def prior_install():
    subprocess.run(['wget','-O','./Prior/Opn_median_mm9.bed','https://github.com/SUwonglab/PECA/blob/master/Prior/Opn_median_mm9.bed'])
    subprocess.run(['wget','-O','./Prior/Opn_median_mm10.bed','https://github.com/SUwonglab/PECA/blob/master/Prior/Opn_median_mm10.bed'])
    subprocess.run(['wget','-O','./Prior/Opn_median_hg19.bed','https://github.com/SUwonglab/PECA/blob/master/Prior/Opn_median_hg19.bed'])
    subprocess.run(['wget','-O','./Prior/Opn_median_hg38.bed','https://github.com/SUwonglab/PECA/blob/master/Prior/Opn_median_hg38.bed'])
    subprocess.run(['wget','-O','./Prior/RE_gene_corr_mm9.bed','https://github.com/SUwonglab/PECA/blob/master/Prior/RE_gene_corr_mm9.bed'])
    subprocess.run(['wget','-O','./Prior/RE_gene_corr_mm10.bed','https://github.com/SUwonglab/PECA/blob/master/Prior/RE_gene_corr_mm10.bed'])
    subprocess.run(['wget','-O','./Prior/RE_gene_corr_hg19.bed','https://github.com/SUwonglab/PECA/blob/master/Prior/RE_gene_corr_hg19.bed'])
    subprocess.run(['wget','-O','./Prior/RE_gene_corr_hg38.bed','https://github.com/SUwonglab/PECA/blob/master/Prior/RE_gene_corr_hg38.bed']) 
    subprocess.run(['wget','-O','./Prior/Enhancer_RE_gene_corr_hg19.bed','https://github.com/SUwonglab/PECA/blob/master/Prior/Enhancer_RE_gene_corr_hg19.bed'])
    subprocess.run(['wget','-O','./Prior/Enhancer_RE_gene_corr_hg38.bed','https://github.com/SUwonglab/PECA/blob/master/Prior/Enhancer_RE_gene_corr_hg38.bed'])
    subprocess.run(['wget','-O','./Prior/Enhancer_RE_gene_corr_mm10.bed','https://github.com/SUwonglab/PECA/blob/master/Prior/Enhancer_RE_gene_corr_mm10.bed'])
    subprocess.run(['wget','-O','./Prior/Enhancer_RE_gene_corr_mm9.bed','https://github.com/SUwonglab/PECA/blob/master/Prior/Enhancer_RE_gene_corr_mm9.bed'])
    subprocess.run(['wget','-O','./Prior/TFTG_corr_mouse.mat','https://github.com/SUwonglab/PECA/blob/master/Prior/TFTG_corr_mouse.mat'])
    subprocess.run(['wget','-O','./Prior/TFTG_corr_human.mat','https://github.com/SUwonglab/PECA/blob/master/Prior/TFTG_corr_human.mat'])
    