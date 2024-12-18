from django.shortcuts import  render
from englisttohindi.englisttohindi import EngtoHindi
def index(request):
    return render(request,'index.html')

def analyze(request):
    text1=request.GET.get('text1')
    upper=request.GET.get('upper','off')
    lower=request.GET.get('lower','off')
    length = request.GET.get('length', 'off')
    strip=request.GET.get('strip', 'off')
    lstrip=request.GET.get('lstrip', 'off')
    rstrip=request.GET.get('rstrip', 'off')
    englisttohindi=request.GET.get('englisttohindi', 'off')

    print(length)
    if upper == 'on':
        params={'text': text1.upper()}
    elif lower == 'on':
         params={'text': text1.lower()}    
    elif length == 'on':
       params={'text': len(text1)}   
    elif strip == 'on':
         params={'text':text1.strip() }  
    elif lstrip == 'on':
         params={'text': text1.lstrip()} 
    elif rstrip == 'on':
         params={'text': text1.rstrip()}
    elif  englisttohindi == 'on':
        res = EngtoHindi(text1)

        params={'text': res.convert}
                                  
    else:
        params={'text': text1} 

         
    return render(request,'analyze.html',params)


def trancelete(request):
    return render(request,'trancelete.html')