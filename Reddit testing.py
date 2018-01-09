import praw


reddit = praw.Reddit(client_id='yXuNREmVQ7OB6A',
                     client_secret='ToO_zFDTkkkW9vssW5WI2fwRPO4',
                     password='Thomas123',
                     user_agent='Amazing',
                     username='Murlaze')

reddit = praw.Reddit(client_id='yXuNREmVQ7OB6A',
                     client_secret='ToO_zFDTkkkW9vssW5WI2fwRPO4',
                     redirect_uri='http://localhost:8080',
                     user_agent='testscript by /u/fakebot3')
print(reddit.auth.url(['identity'], '...', 'permanent'))
print(reddit.user.me())