from django.forms import ModelForm
from .models import PhotoPost
from django import forms

class PhotoPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        
        Attributes:
            model: モデルのクラス
            fields: フォームで使用するモデルのフィールドを指定
        '''
        model = PhotoPost
        fields = ['category1', 'category2', 'category3', 'title', 'title_image', 'mode1', 'status1', 'ability1', 'gage1','connect_skill1', 'connect_joken1', 'shot_skill1', 'assist_skill1' ,'strike_shot1', 'yujou_combo1', 'fukuyujou_combo1', 'luck_skill1','profile1', 'image1', 'image2', 'image3',
                    'mode2', 'status2', 'ability2', 'gage2', 'connect_skill2', 'connect_joken2', 'shot_skill2', 'assist_skill2', 'strike_shot2', 'yujou_combo2', 'fukuyujou_combo2', 'luck_skill2', 'profile2', 'image4', 'image5', 'image6',]
        widgets = {
            'title': forms.Textarea(attrs={'placeholder':'例）ルシファー', 'rows':1, 'cols':40}),
            'mode1': forms.Textarea(attrs={'placeholder':'例）新生・堕天の王 ルシファー', 'rows':1, 'cols':40}),
            'status1': forms.Textarea(attrs={'placeholder':'例）反射/超砲撃型/妖精', 'rows':1, 'cols':40}),
            'ability1': forms.Textarea(attrs={'placeholder':'例）アンチ転送壁/全属性キラー/バリアM...', 'rows':2, 'cols':40}),
            'gage1': forms.Textarea(attrs={'rows':2, 'cols':40}),
            'connect_skill1': forms.Textarea(attrs={'rows':2, 'cols':40}),
            'connect_joken1': forms.Textarea(attrs={'rows':2, 'cols':40}),
            'shot_skill1': forms.Textarea(attrs={'rows':1, 'cols':40}),
            'assist_skill1': forms.Textarea(attrs={'rows':1, 'cols':40}),
            'strike_shot1': forms.Textarea(attrs={'placeholder':'例）堕天の王の歌で味方を動かし...（20+8ターン）', 'rows':2, 'cols':40}),
            'yujou_combo1': forms.Textarea(attrs={'placeholder':'例）ハイエナジーサークル', 'rows':1, 'cols':40}),
            'fukuyujou_combo1': forms.Textarea(attrs={'rows':1, 'cols':40}),
            'luck_skill1': forms.Textarea(attrs={'rows':1, 'cols':40}),
            'profile1': forms.Textarea(attrs={'placeholder':'例）ストライクワールドの危機を自らの命と引き換えに救ったルシファー。'
                                    '天界でも魔界でも、亡き存在になったと思われていたルシファーだったが...\n\n性格：...\n好きなこと：...', 'rows':8, 'cols':40}),
            'status2': forms.Textarea(attrs={'rows':1, 'cols':40}),
            'mode2': forms.Textarea(attrs={'rows':1, 'cols':40}),
            'ability2': forms.Textarea(attrs={'rows':2, 'cols':40}),
            'gage2': forms.Textarea(attrs={'rows':2, 'cols':40}),
            'connect_skill2': forms.Textarea(attrs={'rows':2, 'cols':40}),
            'connect_joken2': forms.Textarea(attrs={'rows':2, 'cols':40}),
            'shot_skill2': forms.Textarea(attrs={'rows':1, 'cols':40}),
            'assist_skill2': forms.Textarea(attrs={'rows':1, 'cols':40}),
            'strike_shot2': forms.Textarea(attrs={'rows':2, 'cols':40}),
            'yujou_combo2': forms.Textarea(attrs={'rows':1, 'cols':40}),
            'fukuyujou_combo2': forms.Textarea(attrs={'rows':1, 'cols':40}),
            'luck_skill2': forms.Textarea(attrs={'rows':1, 'cols':40}),
            'profile2': forms.Textarea(attrs={'rows':8, 'cols':40}),
        }
