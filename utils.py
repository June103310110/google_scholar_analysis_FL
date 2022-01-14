#!/usr/bin/env python
# coding: utf-8
import requests
from bs4 import BeautifulSoup

def abs_from_www_sciencedirect_com(url): 
    
    website = 'www.sciencedirect.com'
    if url.__contains__(website):
        pass
    else:
        raise KeyError(f'This function is only for web {website}')
    
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r.text
    soup = BeautifulSoup(r.text, 'html.parser')

    res = soup.find_all('div', class_ = 'abstract author')[0]
    
    return res.get_text()

#abs_from_www_sciencedirect_com(url)

def abs_from_academic_oup_com(url): 
    
    website = 'academic.oup.com'
    if url.__contains__(website):
        pass
    else:
        raise KeyError(f'This function is only for web {website}')
        
        
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    res = soup.find_all('section', class_ = 'abstract')
    # res.find('div', class_='sec')
    abstract = ''
    for sec in res:
    #     sec.find('div', class_='sec')
        for sub_sec in sec:
            a = sub_sec.contents[0].get_text()
            b = sub_sec.contents[1].get_text()
            abstract += a+' '
            abstract += b
    return abstract
# abs_from_academic_oup_com(url)


# In[460]:


def abs_from_openaccess_thecvf_com(url): 

    website = 'openaccess.thecvf.com'
    if url.__contains__(website):
        pass
    else:
        raise KeyError(f'This function is only for web {website}')

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    res = soup.find_all('div', id='abstract')
    abstract = ""
    for i in res:
#         print(i)
        abstract+= i.get_text()
    return abstract.replace('\n', '').strip() #.split('Abstract: ')[1]

# abs_from_openaccess_thecvf_com(url)


# In[459]:


def abs_from_proceedings_neurips_cc(url): 

    website = 'proceedings.neurips.cc'
    if url.__contains__(website):
        pass
    else:
        raise KeyError(f'This function is only for web {website}')

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    res= soup.find_all('p')

    max_length = max([len(i.get_text()) for i in res])
    for i in res:
        if len(i.get_text()) == max_length:
#             print(i.get_text())  
            return i.get_text()

# abs_from_proceedings_neurips_cc(url)


# In[458]:


def abs_from_link_springer_com(url): 

    website = 'link.springer.com'
    if url.__contains__(website):
        pass
    else:
        raise KeyError(f'This function is only for web {website}')

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    res = soup.find_all('div',  class_='c-article-section__content', id='Abs1-content')
    abstract = ""
    for i in res:
#         print(i)
        abstract+= i.get_text()
    return abstract #.split('Abstract: ')[1].replace('\n', '').strip()

# abs_from_link_springer_com(url)


# In[457]:


def abs_from_dl_acm_org(url): 

    website = 'dl.acm.org'
    if url.__contains__(website):
        pass
    else:
        raise KeyError(f'This function is only for web {website}')

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    res = soup.find_all('div',  class_="abstractSection abstractInFull")
    abstract = ""
    for i in res:
#         print(i)
        abstract+= i.get_text()
    return abstract #.split('Abstract: ')[1].replace('\n', '').strip()

# abs_from_dl_acm_org(url)


# In[456]:


def abs_from_arxiv_org(url): 

    website = 'arxiv.org'
    if url.__contains__(website):
        pass
    else:
        raise KeyError(f'This function is only for web {website}')

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    res = soup.find_all('blockquote',  class_="abstract mathjax")
    abstract = ""
    for i in res:
#         print(i)
        abstract+= i.get_text()
    return abstract.split('Abstract: ')[1].replace('\n', '').strip()

# abs_from_arxiv_org(url)


# In[455]:


def abs_from_www_pnas_org(url): 

    website = 'www.pnas.org'
    if url.__contains__(website):
        pass
    else:
        raise KeyError(f'This function is only for web {website}')

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    res = soup.find_all('div',  class_="section abstract")
    abstract = ""
    for i in res:
    #         print(i.get_text())
        abstract+= i.get_text()
    return abstract

# abs_from_www_pnas_org(url)


# In[454]:


def abs_from_www_usenix_org(url): 
    website = 'www.usenix.org'
    if url.__contains__(website):
        pass
    else:
        raise KeyError(f'This function is only for web {website}')
        
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    res = soup.find_all('div',  class_="field field-name-field-paper-description field-type-text-long field-label-above")
    abstract = ""
    for i in res:
#         print(i.get_text())
        abstract+= i.get_text()
    return abstract
#     soup_ = BeautifulSoup(i, 'html.parser')

# abs_from_www_usenix_org(url)


# In[453]:


# def abs_from_ieeexplore_ieee_org(url): 
# print(url)
def abs_from_www_nature_com(url): 
    website = 'www.nature.com'
    if url.__contains__(website):
        pass
    else:
        raise KeyError(f'This function is only for web {website}')
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    res = soup.find_all('div',  class_="c-article-section__content")
    return [ i.get_text().strip() for i in res][0]

# abs_from_www_nature_com(url)


# In[448]:

#     pass
def abs_from_ieeexplore_ieee_org(url): 
    website = 'ieeexplore.ieee.org'
    if url.__contains__(website):
        pass
    else:
        raise KeyError(f'This function is only for web {website}')
    r = requests.get(url)
    abstract = r.text.split('meta property="og:description"')[1].split('content="')[1].split('"')[0]
    return abstract
# abs_from_ieeexplore_ieee_org(url)


# In[449]:


def abs_from_proceedings_mlr_press(url):
    website = 'proceedings.mlr.press'
    if url.__contains__(website):
        pass
    else:
        raise KeyError(f'This function is only for web {website}')
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')
    res = soup.find_all('div',  class_="abstract")
    return [ i.get_text().strip() for i in res][0]


# abs_from_proceedings_mlr_press(url)


# In[447]:


# def get_des(dic_gs_rs):
#     des = []
#     for i in dic_gs_rs:
#         a = i.get_text()
#         des.append(a)
#     return des
# if __name__ == '__main__':
#     res = get_des(soup.find_all('div',  class_="gs_rs"))
#     print(res)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




