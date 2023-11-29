from django.contrib import admin
# CustomUserをインポート
from .models import Category1, Category2, Category3, PhotoPost

class Category1Admin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス

    '''
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

class Category2Admin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス

    '''
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

class Category3Admin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス

    '''
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

class PhotoPostAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス

    '''
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

# Django管理サイトにCategory1、Category1Adminを登録する
admin.site.register(Category1, Category1Admin)

# Django管理サイトにCategory2、Category2Adminを登録する
admin.site.register(Category2, Category2Admin)

# Django管理サイトにCategory3、Category3Adminを登録する
admin.site.register(Category3, Category3Admin)

# Django管理サイトにPhotoPost、PhotoPostAdminを登録する
admin.site.register(PhotoPost, PhotoPostAdmin)
