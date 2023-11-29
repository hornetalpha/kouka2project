from django.shortcuts import render
# django.views.genericからTemplateView、ListViewをインポート
from django.views.generic import TemplateView, ListView
# django.views.genericからCreateViewをインポート
from django.views.generic import CreateView
# django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
# formsモジュールからPhotoPostFormをインポート
from .forms import PhotoPostForm
# method_decoratorをインポート
from django.utils.decorators import method_decorator
# login_requiredをインポート
from django.contrib.auth.decorators import login_required
# modelsモジュールからモデルPhotoPostをインポート
from .models import PhotoPost
# django.views.genericからDetailViewをインポート
from django.views.generic import DetailView
# django.views.genericからDeleteViewをインポート
from django.views.generic import DeleteView
# django.views.genericからUpdateViewをインポート
from django.views.generic import UpdateView

class IndexView(ListView):
    '''トップページのビュー
    '''
    # index.htmlをレンダリングする
    template_name = 'index.html'
    # モデルPhotoPostのオブジェクトにorder_by()を適用して
    # 投稿日時の降順で並べ替える
    queryset = PhotoPost.objects.order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 12

# デコレーターにより、CreatePhotoViewへのアクセスはログインユーザーに限定される
# ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    '''投稿写真ページのビュー
    
    PhotoPostFormで定義されているモデルとフィールドと連携して
    投稿データをデータベースに登録する
    
    Attributes:
        form_class: モデルとフィールドが登録されたフォームクラス
        template_name: レンダリングするテンプレート
        success_url: データベースへの登録完了後のリダイレクト先
    '''
    # forms.pyのPhotoPostFormをフォームクラスとして登録
    form_class = PhotoPostForm
    # レンダリングするテンプレート
    template_name = "post_photo.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('kouka2:post_done')

    def form_valid(self, form):
        '''CreateViewクラスのform_validをオーバーライド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う
        
        parameters:
            form(django.forms.Form):
                form_classに格納されているPhotoPostFormオブジェクト
        Return:
            HttpResponseRedirectオブジェクト
                スーパークラスのform_valid()の戻り値を返すことで、
                success_urlで設定されているURLにリダイレクトさせる
        '''
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    '''投稿完了ページのビュー
    
    Attributes:
        template_name: レンダリングするテンプレート
    '''
    # post_success.htmlをレンダリングする
    template_name = 'post_success.html'

class Category1View(ListView):
    '''カテゴリ1ページのビュー
    
    Attributes
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレンダリングする
    template_name = 'index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 12

    def get_queryset(self):
        '''クエリを実行する
        
        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する
        
        Returns:
            クエリによって取得されたレコード
        '''
        # self.kwargsでキーワードの辞書を取得し、
        # categoryキーの値(Categorysテーブルのid)を取得
        category_id = self.kwargs['category1']
        # filter(フィールド名=id)で絞り込む
        categories = PhotoPost.objects.filter(
            category1=category_id).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return categories

class Category2View(ListView):
    '''カテゴリ2ページのビュー
    
    Attributes
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレンダリングする
    template_name = 'index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 12

    def get_queryset(self):
        '''クエリを実行する
        
        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する
        
        Returns:
            クエリによって取得されたレコード
        '''
        # self.kwargsでキーワードの辞書を取得し、
        # categoryキーの値(Categorysテーブルのid)を取得
        category_id = self.kwargs['category2']
        # filter(フィールド名=id)で絞り込む
        categories = PhotoPost.objects.filter(
            category2=category_id).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return categories

class Category3View(ListView):
    '''カテゴリ3ページのビュー
    
    Attributes
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレンダリングする
    template_name = 'index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 12

    def get_queryset(self):
        '''クエリを実行する
        
        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する
        
        Returns:
            クエリによって取得されたレコード
        '''
        # self.kwargsでキーワードの辞書を取得し、
        # categoryキーの値(Categorysテーブルのid)を取得
        category_id = self.kwargs['category3']
        # filter(フィールド名=id)で絞り込む
        categories = PhotoPost.objects.filter(
            category3=category_id).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return categories

class UserView(ListView):
    '''ユーザー投稿一覧ページのビュー
    
    Attributes
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレンダリングする
    template_name = 'index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 12

    def get_queryset(self):
        '''クエリを実行する
        
        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する
        
        Returns:
            クエリによって取得されたレコード
        '''
        # self.kwargsでキーワードの辞書を取得し、
        # userキーの値(ユーザーテーブルのid)を取得
        user_id = self.kwargs['user']
        # filter(フィールド名=id)で絞り込む
        user_list = PhotoPost.objects.filter(
            user=user_id).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return user_list

class DetailView(DetailView):
    '''詳細ページのビュー
    
    投稿記事の詳細を表示するのでDetailViewを継承する
    Attributes:
        template_name: レンダリングするテンプレート
        model: モデルのクラス
    '''
    # detail.htmlをレンダリングする
    template_name = 'detail.html'
    # クラス変数modelにPhotoPostを設定
    model = PhotoPost

class MypageView(ListView): 
    '''マイページのビュー
    
    Attributes
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    # mypage.htmlをレンダリングする
    template_name = 'mypage.html'
    # 1ページに表示するレコードの件数
    paginate_by = 12

    def get_queryset(self):
        '''クエリを実行する
        
        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する
        
        Returns:
            クエリによって取得されたレコード
        '''
        # 現在ログインしているユーザー名はHttpRequest.userに格納されている
        # filter(userフィールド=userオブジェクト)で絞り込む
        queryset = PhotoPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return queryset

class PhotoDeleteView(DeleteView):
    '''レコードの削除を行うビュー
    
    Attributes:
        model: モデル
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
        success_url: 削除完了後のリダイレクト先のURL
    '''
    # 操作の対象はPhotoPostモデル
    model = PhotoPost
    # photo_delete.htmlをレンダリングする
    template_name = 'photo_delete.html'
    # 処理完了後にマイページにリダイレクト
    success_url = reverse_lazy('kouka2:mypage')

    def delete(self, request, *args, **kwargs):
        '''レコードの削除を行う
        
        Parameters:
            self: PhotoDeleteViewオブジェクト
            request: WSGIRequest(HttpRequest)オブジェクト
            args: 引数として渡される辞書(dict)
            kwargs: キーワード付きの辞書(dict)
                {'pk': 21}のようにレコードのidが渡される
                
        Returns:
            HttpResponseRedirect(success_url)を渡して
            success_urlにリダイレクト
        '''
        # スーパークラスのdelete()を実行
        return super().delete(request, *args, **kwargs)

class ElementSortView(ListView):
    '''属性ソートのビュー
    
    Attributes
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレンダリングする
    template_name = 'index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 12

    def get_queryset(self):
        '''クエリを実行する
        
        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する
        
        Returns:
            クエリによって取得されたレコード
        '''
        # 現在ログインしているユーザー名はHttpRequest.userに格納されている
        # filter(userフィールド=userオブジェクト)で絞り込む
        queryset = PhotoPost.objects.order_by('category1', '-posted_at')
        # クエリによって取得されたレコードを返す
        return queryset

class MyCategory1View(ListView):
    '''マイページのカテゴリ1ページのビュー
    
    Attributes
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    # mypage.htmlをレンダリングする
    template_name = 'mypage.html'
    # 1ページに表示するレコードの件数
    paginate_by = 12

    def get_queryset(self):
        '''クエリを実行する
        
        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する
        
        Returns:
            クエリによって取得されたレコード
        '''
        # self.kwargsでキーワードの辞書を取得し、
        # categoryキーの値(Categorysテーブルのid)を取得
        category_id = self.kwargs['category1']
        # filter(フィールド名=id)で絞り込む
        categories = PhotoPost.objects.filter(
            category1=category_id, user=self.request.user).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return categories

class MyCategory2View(ListView):
    '''マイページのカテゴリ2ページのビュー
    
    Attributes
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    # mypage.htmlをレンダリングする
    template_name = 'mypage.html'
    # 1ページに表示するレコードの件数
    paginate_by = 12

    def get_queryset(self):
        '''クエリを実行する
        
        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する
        
        Returns:
            クエリによって取得されたレコード
        '''
        # self.kwargsでキーワードの辞書を取得し、
        # categoryキーの値(Categorysテーブルのid)を取得
        category_id = self.kwargs['category2']
        # filter(フィールド名=id)で絞り込む
        categories = PhotoPost.objects.filter(
            category2=category_id, user=self.request.user).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return categories

class MyCategory3View(ListView):
    '''マイページのカテゴリ3ページのビュー
    
    Attributes
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    # mypage.htmlをレンダリングする
    template_name = 'mypage.html'
    # 1ページに表示するレコードの件数
    paginate_by = 12

    def get_queryset(self):
        '''クエリを実行する
        
        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する
        
        Returns:
            クエリによって取得されたレコード
        '''
        # self.kwargsでキーワードの辞書を取得し、
        # categoryキーの値(Categorysテーブルのid)を取得
        category_id = self.kwargs['category3']
        # filter(フィールド名=id)で絞り込む
        categories = PhotoPost.objects.filter(
            category3=category_id, user=self.request.user).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return categories

class MyElementSortView(ListView):
    '''マイページの属性ソートのビュー
    
    Attributes
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    # mypsge.htmlをレンダリングする
    template_name = 'mypage.html'
    # 1ページに表示するレコードの件数
    paginate_by = 12

    def get_queryset(self):
        '''クエリを実行する
        
        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する
        
        Returns:
            クエリによって取得されたレコード
        '''
        # 現在ログインしているユーザー名はHttpRequest.userに格納されている
        # filter(userフィールド=userオブジェクト)で絞り込む
        queryset = PhotoPost.objects.filter(
            user=self.request.user, ).order_by('category1', '-posted_at')
        # クエリによって取得されたレコードを返す
        return queryset

class PhotoUpdateView(UpdateView):
    template_name = 'photo_update.html'
    model = PhotoPost
    fields = ['category1', 'category2', 'category3', 'title', 'title_image', 'mode1', 'status1', 'ability1', 'gage1','connect_skill1', 'connect_joken1', 'shot_skill1', 'assist_skill1' ,'strike_shot1', 'yujou_combo1', 'fukuyujou_combo1', 'luck_skill1','profile1', 'image1', 'image2', 'image3',
                    'mode2', 'status2', 'ability2', 'gage2', 'connect_skill2', 'connect_joken2', 'shot_skill2', 'assist_skill2', 'strike_shot2', 'yujou_combo2', 'fukuyujou_combo2', 'luck_skill2', 'profile2', 'image4', 'image5', 'image6',]
    success_url = reverse_lazy('kouka2:update_done')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)

class UpdateSuccessView(TemplateView):
    '''編集完了ページのビュー
    
    Attributes:
        template_name: レンダリングするテンプレート
    '''
    # update_success.htmlをレンダリングする
    template_name = 'update_success.html'

class OldSortView(ListView):
    '''昇順ページのビュー
    '''
    # index.htmlをレンダリングする
    template_name = 'index.html'
    # モデルPhotoPostのオブジェクトにorder_by()を適用して
    # 投稿日時の昇順で並べ替える
    queryset = PhotoPost.objects.order_by('posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 12

class MyOldSortView(ListView):
    '''マイページの昇順ページビュー
    '''
    # mypage.htmlをレンダリングする
    template_name = 'mypage.html'
    # モデルPhotoPostのオブジェクトにorder_by()を適用して
    # 投稿日時の昇順で並べ替える
    queryset = PhotoPost.objects.order_by('posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 12

    def get_queryset(self):
        '''クエリを実行する
        
        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する
        
        Returns:
            クエリによって取得されたレコード
        '''
        # 現在ログインしているユーザー名はHttpRequest.userに格納されている
        # filter(userフィールド=userオブジェクト)で絞り込む
        queryset = PhotoPost.objects.filter(
            user=self.request.user).order_by('posted_at')
        # クエリによって取得されたレコードを返す
        return queryset

class SearchView(ListView):
    '''トップページのサーチビュー
    '''
    # index.htmlをレンダリングする
    template_name = 'index.html'
    # モデルPhotoPostのオブジェクトにorder_by()を適用して
    # 投稿日時の降順で並べ替える
    queryset = PhotoPost.objects.order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 12

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET

        if q := query.get('q'): 
            queryset = queryset.filter(title__icontains=q)

        return queryset.order_by('-posted_at')

class MySearchView(ListView):
    '''マイページのサーチビュー
    '''
    # mypage.htmlをレンダリングする
    template_name = 'mypage.html'
    # モデルPhotoPostのオブジェクトにorder_by()を適用して
    # 投稿日時の降順で並べ替える
    queryset = PhotoPost.objects.order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 12

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET

        if q := query.get('q'): 
            queryset = queryset.filter(title__icontains=q)

        return queryset.filter(user=self.request.user).order_by('-posted_at')