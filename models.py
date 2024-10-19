from sqlalchemy import Column, Integer, String, ForeignKey, Text, Table, Boolean
from sqlalchemy.orm import relationship
from databsefile.db_conf import Base 


post_tags = Table('post_tags', Base.metadata,
                  Column('post_id', ForeignKey('posts.id'), primary_key=True),
                  Column('tag_id', ForeignKey('tags.id'), primary_key=True))


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)
    is_super_user = Column(Boolean, default=False)
    admin_id = Column(Integer, ForeignKey("users.id"))
    admin = relationship("User", remote_side=[id], backref="subordinates")
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', is_admin={self.is_admin}, is_super_user={self.is_super_user})>"


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(Text, nullable=False)
    image = Column(String, nullable=True)  # Path to the image
    likes = Column(Integer, default=0)
    dislikes = Column(Integer, default=0)
    views = Column(Integer, default=0)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="posts")
    tags = relationship("Tag", secondary=post_tags, back_populates="posts")

Category.posts = relationship("Post", back_populates="category")
Tag.posts = relationship("Post", secondary=post_tags, back_populates="tags")
