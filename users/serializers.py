from users.models import User, Contract, ClientProfile, Identification, Position
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ['id', 'name']

class ContractSerializer(serializers.ModelSerializer):

    position = serializers.PrimaryKeyRelatedField(required=True, queryset=Position.objects.all())
    
    class Meta:
        model = Contract
        fields = ['id', 'salary', 'join_date', 'end_date', 'is_active', 'position']
        depth = 1

class EmployeeSerializer(serializers.ModelSerializer):

    contract = ContractSerializer()
    identification = serializers.CharField(required=True)
    phone = PhoneNumberField()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'phone', 'last_login', 'date_joined', 'is_staff', 'is_active', 'identification', 'contract']
        read_only_fields = ['is_active', 'is_staff', 'date_joined', 'last_login']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        depth = 1

    #override was needed due to identification phone and position not being correctly serialized
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'username': instance.username,
            'email': instance.email,
            'phone': instance.phone.raw_input,
            'last_login': instance.last_login,
            'date_joined': instance.date_joined,
            'is_staff': instance.is_staff,
            'is_active': instance.is_active,
            'identification': instance.identification.id,
            'contract': {
                'id': instance.contract.id,
                'salary': instance.contract.salary,
                'join_date': instance.contract.join_date,
                'end_date': instance.contract.end_date,
                'is_active': instance.contract.is_active,
                'position': instance.contract.position.name
            }
        }

    def create(self, validated_data):
        
        contract_data = validated_data.pop('contract')
        identification_data = validated_data.pop('identification')
        
        identification = Identification.objects.create(id=identification_data)

        user = User.objects.create(identification=identification, is_staff=True, **validated_data)
        
        #hash password instead of saving it in plain text
        user.set_password(user.password)

        contract = Contract.objects.create(user=user,  **contract_data)
        contract.save()
        
        user.save()
        return user

    def update(self, instance, validated_data):
        
        #get contract of user
        contract = instance.contract
        contract_data = validated_data.pop('contract')

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        #update password if it axists on the request
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        
        #update contract data
        if contract_data is not None:
            contract.salary = contract_data.get('salary', contract.salary)
            contract.join_date = contract_data.get('join_date', contract.join_date)
            contract.end_date = contract_data.get('end_date', contract.end_date)
            contract.is_active = contract_data.get('is-active', contract.is_active)
            contract.position = contract_data.get('position', contract.position)

            contract.save()
        
        instance.save()

        return instance

class ClientProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClientProfile
        fields = ['id', 'address']

class ClientSerializer(serializers.ModelSerializer):

    client_profile = ClientProfileSerializer()
    identification = serializers.CharField(required=True)
    phone = PhoneNumberField()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'phone', 'last_login', 'date_joined', 'is_staff', 'is_active', 'identification', 'client_profile']
        read_only_fields = ['is_active', 'is_staff', 'date_joined', 'last_login']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        depth = 1
    
    #override was needed due to identification and phone not being correctly serialized
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'username': instance.username,
            'email': instance.email,
            'phone': instance.phone.raw_input,
            'last_login': instance.last_login,
            'date_joined': instance.date_joined,
            'is_staff': instance.is_staff,
            'is_active': instance.is_active,
            'identification': instance.identification.id,
            'client_profile': {
                'id': instance.client_profile.id,
                'address': instance.client_profile.address,
            }
        }

    def create(self, validated_data):
        
        profile_data = validated_data.pop('client_profile')
        identification_data = validated_data.pop('identification')
        
        identification = Identification.objects.create(id=identification_data)

        user = User.objects.create(identification=identification, **validated_data)
        
        #hash password instead of saving it in plain text
        user.set_password(user.password)

        profile = ClientProfile.objects.create(user=user, **profile_data)
        profile.save()
        
        user.save()
        return user

    def update(self, instance, validated_data):
        
        #get profile of user
        profile = instance.client_profile
        profile_data = validated_data.pop('client_profile')

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        #update password if it axists on the request
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        
        #update profile data
        if profile is not None:
            profile.address = profile_data.get('address', profile.address)

            profile.save()
        
        instance.save()

        return instance

