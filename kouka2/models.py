from django.db import models
# accountsアプリのmodelsモジュールからCustomUserをインポート
from accounts.models import CustomUser


class Category1(models.Model):
    '''投稿する写真のカテゴリを管理するモデル
    '''
    # カテゴリ名のフィールド
    title = models.CharField(
        verbose_name='カテゴリ', #フィールドのタイトル
        max_length=20)
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):カテゴリ名
        '''
        return self.title

class Category2(models.Model):
    '''投稿する写真のカテゴリを管理するモデル
    '''
    # カテゴリ名のフィールド
    title = models.CharField(
        verbose_name='カテゴリ', #フィールドのタイトル
        max_length=20)
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):カテゴリ名
        '''
        return self.title

class Category3(models.Model):
    '''投稿する写真のカテゴリを管理するモデル
    '''
    # カテゴリ名のフィールド
    title = models.CharField(
        verbose_name='カテゴリ', #フィールドのタイトル
        max_length=20)
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):カテゴリ名
        '''
        return self.title

class PhotoPost(models.Model):
    '''投稿されたデータを管理するモデル
    '''
    # CustomUserモデル(のuser_id)とPhotoPostモデルを
    # 1対多の関係で結び付ける
    # CustomUserが親でPhotoPostが子の関係となる
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='ユーザー',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
        )
    # Category1モデル(のtitle)とPhotoPostモデルを
    # 1対多の関係で結び付ける
    # Category1が親でPhotoPostが子の関係となる
    category1 = models.ForeignKey(
        Category1,
        # フィールドのタイトル
        verbose_name='属性',
        # カテゴリに関連付けられた投稿データが存在する場合は
        # そのカテゴリを削除できないようにする
        on_delete=models.PROTECT
        )
    # Category2モデル(のtitle)とPhotoPostモデルを
    # 1対多の関係で結び付ける
    # Category2が親でPhotoPostが子の関係となる
    category2 = models.ForeignKey(
        Category2,
        # フィールドのタイトル
        verbose_name='進化状態',
        # カテゴリに関連付けられた投稿データが存在する場合は
        # そのカテゴリを削除できないようにする
        on_delete=models.PROTECT
        )
    # Category3モデル(のtitle)とPhotoPostモデルを
    # 1対多の関係で結び付ける
    # Category3が親でPhotoPostが子の関係となる
    category3 = models.ForeignKey(
        Category3,
        # フィールドのタイトル
        verbose_name='入手方法',
        # カテゴリに関連付けられた投稿データが存在する場合は
        # そのカテゴリを削除できないようにする
        on_delete=models.PROTECT
        )
    # タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル名', #フィールドのタイトル
        max_length=200          #最大文字数は200
        )
    title_image = models.ImageField(
        verbose_name='タイトル画像', #フィールドのタイトル
        upload_to = 'title_img'     #MEDIA_ROOT以下のphotosにファイルを保存
        )
    # 進化形態用のフィールド
    mode1 = models.CharField(
        verbose_name='進化形態の名前', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        )
    # ステータス用のフィールド
    status1 = models.CharField(
        verbose_name='撃種/戦型/種族', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        )
    # アビリティ用のフィールド
    ability1 = models.CharField(
        verbose_name='アビリティ', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        )
    # ゲージ用のフィールド
    gage1 = models.CharField(
        verbose_name='ゲージアビリティ', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # コネクトスキル用のフィールド
    connect_skill1 = models.CharField(
        verbose_name='コネクトスキル', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # コネクトスキル条件用のフィールド
    connect_joken1 = models.CharField(
        verbose_name='コネクトスキル条件', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # ショットスキル用のフィールド
    shot_skill1 = models.CharField(
        verbose_name='ショットスキル', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # アシストスキル用のフィールド
    assist_skill1 = models.CharField(
        verbose_name='アシストスキル', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # ストライクショット用のフィールド
    strike_shot1 = models.CharField(
        verbose_name='ストライクショット', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        )
     # 友情コンボ用のフィールド
    yujou_combo1 = models.CharField(
        verbose_name='友情コンボ', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        )
    # 副友情コンボ用のフィールド
    fukuyujou_combo1 = models.CharField(
        verbose_name='副友情コンボ', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
     # ラックスキル用のフィールド
    luck_skill1 = models.CharField(
        verbose_name='ラックスキル', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # プロフィール用のフィールド
    profile1 = models.TextField(
        verbose_name='profile', #フィールドのタイトル
        )
    
    # イメージのフィールド1
    image1 = models.ImageField(
        verbose_name='通常イラスト', #フィールドのタイトル
        upload_to = 'photos'     #MEDIA_ROOT以下のphotosにファイルを保存
        )
    # イメージのフィールド2
    image2 = models.ImageField(
        verbose_name='季節限定/書き下ろしイラスト', #フィールドのタイトル
        upload_to = 'photos',    #MEDIA_ROOT以下のphotosにファイルを保存
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # イメージのフィールド2
    image3 = models.ImageField(
        verbose_name='MVイラスト', #フィールドのタイトル
        upload_to = 'photos',    #MEDIA_ROOT以下のphotosにファイルを保存
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # 進化形態用のフィールド
    mode2 = models.CharField(
        verbose_name='進化形態の名前', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )

    # ステータス用のフィールド
    status2 = models.CharField(
        verbose_name='撃種/戦型/種族', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # アビリティ用のフィールド
    ability2 = models.CharField(
        verbose_name='アビリティ', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # ゲージ用のフィールド
    gage2 = models.CharField(
        verbose_name='ゲージアビリティ', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # コネクトスキル用のフィールド
    connect_skill2 = models.CharField(
        verbose_name='コネクトスキル', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # コネクトスキル条件用のフィールド
    connect_joken2 = models.CharField(
        verbose_name='コネクトスキル条件', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # ショットスキル用のフィールド
    shot_skill2 = models.CharField(
        verbose_name='ショットスキル', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # アシストスキル用のフィールド
    assist_skill2 = models.CharField(
        verbose_name='アシストスキル', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # ストライクショット用のフィールド
    strike_shot2 = models.CharField(
        verbose_name='ストライクショット', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
     # 友情コンボ用のフィールド
    yujou_combo2 = models.CharField(
        verbose_name='友情コンボ', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # 副友情コンボ用のフィールド
    fukuyujou_combo2 = models.CharField(
        verbose_name='副友情コンボ', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
     # ラックスキル用のフィールド
    luck_skill2 = models.CharField(
        verbose_name='ラックスキル', #フィールドのタイトル
        max_length=200,          #最大文字数は200
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # プロフィール用のフィールド
    profile2 = models.TextField(
        verbose_name='プロフィール', #フィールドのタイトル
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # イメージのフィールド2
    image4 = models.ImageField(
        verbose_name='通常イラスト', #フィールドのタイトル
        upload_to = 'photos',    #MEDIA_ROOT以下のphotosにファイルを保存
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # イメージのフィールド2
    image5 = models.ImageField(
        verbose_name='季節限定/書き下ろしイラスト', #フィールドのタイトル
        upload_to = 'photos',    #MEDIA_ROOT以下のphotosにファイルを保存
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # イメージのフィールド2
    image6 = models.ImageField(
        verbose_name='MVイラスト', #フィールドのタイトル
        upload_to = 'photos',    #MEDIA_ROOT以下のphotosにファイルを保存
        blank=True,              #フィールド値の設定は必須でない
        null=True                #データベースにnullが保存されることを許容
        )
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',  #フィールドのタイトル
        auto_now_add=True        #日時を自動追加
        )

    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):投稿記事のタイトル
        '''
        return self.title
